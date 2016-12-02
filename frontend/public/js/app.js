var app = angular.module('myApp', ['ui.router']);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
  $urlRouterProvider.otherwise('/');
  $stateProvider
    .state('home', {
      url: '/',
      templateUrl: 'templates/homepage.html',
      controller: 'HomeCtrl'
    })
    .state('login', {
      url: '/login/',
      templateUrl: 'templates/login.html',
      controller: 'AuthCtrl'
    })
    .state('logout', {
      url: '/logout/',
      template: '<div ng-controller="AuthCtrl" data-ng-init="logout()"></div>',
      controller: 'AuthCtrl'
    })
    .state('lunch_day', {
      url: '/lunch/day/',
      templateUrl: 'templates/lunch_day.html',
      controller: 'LunchDayCtrl'
    })
    .state('lunch_day_particular', {
      url: '/lunch/day/:date/',
      templateUrl: 'templates/lunch_day.html',
      controller: 'LunchDayCtrl'
    })
    .state('schedule', {
      url: '/schedule/',
      templateUrl: 'templates/schedule.html',
      controller: 'ScheduleCtrl'
    })
    .state('schedule_particular', {
      url: '/schedule/:year/:month/',
      templateUrl: 'templates/schedule.html',
      controller: 'ScheduleCtrl'
    })
    .state('lunch_month', {
      url: '/lunch/month/',
      templateUrl: 'templates/lunch_month.html',
      controller: 'LunchMonthCtrl'
    })
    .state('lunch_month_particular', {
      url: '/lunch/month/:year/:month/',
      templateUrl: 'templates/lunch_month.html',
      controller: 'LunchMonthCtrl'
    })
    .state('admin_holiday', {
      url: '/admin/holiday/',
      templateUrl: 'templates/admin_holiday.html',
      controller: 'AdminHolidayCtrl'
    })
    .state('admin_schedule', {
      url: '/admin/schedule/',
      templateUrl: 'templates/admin_schedule.html',
      controller: 'AdminScheduleCtrl'
    })
    .state('admin_users_lunch', {
      url: '/admin/users/lunch/',
      templateUrl: 'templates/admin_users_lunch.html',
      controller: 'AdminUserLunchCtrl'
    })
    .state('admin_single_user_lunch', {
      url: '/admin/users/lunch/:id/',
      templateUrl: 'templates/admin_single_user_lunch.html',
      controller: 'AdminSingleUserLunchCtrl'
    })
    .state('admin_users_working', {
      url: '/admin/users/working/',
      templateUrl: 'templates/admin_users_working.html',
      controller: 'AdminUserWorkingCtrl'
    })
    .state('admin_single_user_working', {
      url: '/admin/users/working/:id/',
      templateUrl: 'templates/admin_single_user_working.html',
      controller: 'AdminSingleUserWorkingCtrl'
    })
    .state('admin_mealprice', {
      url: '/admin/mealprice/',
      templateUrl: 'templates/admin_mealprice.html',
      controller: 'AdminMealPriceCtrl'
    })
    .state('admin_users_create', {
      url: '/admin/users/create/',
      templateUrl: 'templates/admin_users_create.html',
      controller: 'AdminUsersCreateCtrl'
    })
    .state('admin_users', {
      url: '/admin/users/',
      templateUrl: 'templates/admin_users.html',
      controller: 'AdminUsersCtrl'
    })
    .state('admin_users_update', {
      url: '/admin/users/:id/',
      templateUrl: 'templates/admin_users_update.html',
      controller: 'AdminUsersUpdateCtrl'
    })
    .state('admin_generate_schedule', {
      url: '/admin/schedule/generate/',
      templateUrl: 'templates/admin_schedule_generate.html',
      controller: 'AdminScheduleGenerateCtrl'
    })
    .state('admin_lunch_generate', {
      url: '/admin/lunch/generate/',
      templateUrl: 'templates/admin_lunch_generate.html',
      controller: 'AdminLunchGenerateCtrl'
    })
    .state('user_lunch_register', {
      url: '/user/lunch/register/',
      templateUrl: 'templates/user_lunch_register.html',
      controller: 'UserLunchRegisterCtrl'
    })
    .state('user_working_register', {
      url: '/user/working/register/',
      templateUrl: 'templates/user_working_register.html',
      controller: 'UserWorkingRegisterCtrl'
    })
    .state('user_lunch_summary', {
      url: '/user/lunch/summary/',
      templateUrl: 'templates/user_lunch_summary.html',
      controller: 'UserLunchSummaryCtrl'
    })
    .state('user_particular_lunch_summary', {
      url: '/user/lunch/summary/:year/:month/',
      templateUrl: 'templates/user_lunch_summary.html',
      controller: 'UserLunchSummaryCtrl'
    })
    .state('user_personal_schedule', {
      url: '/user/working/schedule/',
      templateUrl: 'templates/user_personal_schedule.html',
      controller: 'UserPersonalScheduleCtrl'
    })
    .state('user_particular_personal_schedule', {
      url: '/user/working/schedule/:year/:month/',
      templateUrl: 'templates/user_personal_schedule.html',
      controller: 'UserPersonalScheduleCtrl'
    })
    .state('user_settings', {
      url: '/user/settings/',
      templateUrl: 'templates/user_settings.html',
      controller: 'UserSettingsCtrl'
    });
    // $locationProvider.html5Mode(true);
});

app.config(function($httpProvider, $windowProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

  var API_URL = 'http://127.0.0.1:8000/';

	function apiInterceptor($q) {
  	return {
    	request: function (config) {
      	var url = config.url;
      	// ignore template requests
      	if (url.substr(url.length - 5) == '.html') {
        	return config || $q.when(config);
      	}
      	config.url = API_URL + config.url;
      		return config || $q.when(config);
    	}
  	}
	}
	$httpProvider.interceptors.push(apiInterceptor);

	var $window = $windowProvider.$get();
	$httpProvider.defaults.headers.common['one-token'] = $window.localStorage.getItem('token');
});

app.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.run(function ($rootScope, $state, $http, $window) {
  $rootScope.$on('$stateChangeSuccess', function() {
      if ($state.current.name == 'home')
        jQuery('html, body').animate({ scrollTop: 0 }, 200);
  });

  if ($window.localStorage.getItem('token') != null) {
    $http.get('api/members/profile/').then(
      function(response) {
        $window.localStorage.setItem('id', response.data.id);
        $window.localStorage.setItem('username', response.data.username);
        $window.localStorage.setItem('is_admin', response.data.is_admin);
        $window.localStorage.setItem('has_working_schedule', response.data.has_working_schedule);
        $window.localStorage.setItem('date_joined', response.data.date_joined);
        $window.localStorage.setItem('email', response.data.email);
        $window.localStorage.setItem('fullname', response.data.fullname);
        $window.localStorage.setItem('last_login', response.data.last_login);
      },
      function(response) {
        // in case of token expires
        if ((response.status == 401) || (response.status == 500))
          $state.go('logout');
      }
    );
  }
});

app.factory('range', function () {
  return {
    getRange: function(start, stop, step) {
      if (typeof stop == 'undefined') {
          // one param defined
          stop = start;
          start = 0;
      }
      if (typeof step == 'undefined') {
          step = 1;
      }
      if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
          return [];
      }
      var result = [];
      for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
          result.push(i);
      }
      return result;
    }
  }
});