app.controller('UserLunchRegisterCtrl', function($rootScope, $http, $scope, $filter, $window) {
	$rootScope.hide = false;
	$scope.id = $window.localStorage.getItem('id');
	$scope.login = $window.localStorage.getItem('login');
	$scope.working = JSON.parse($window.localStorage.getItem('has_working_schedule'));

	if ($scope.login)
		$scope.username = $window.localStorage.getItem('username');
	else
		$scope.username = 'User';

	$rootScope.header = $scope.username + ' | Lunch Request';

	$scope.init = function() {

		if ($scope.login) {

			$http.get('api/lunch/default/'+$scope.id+'/').then(
				function(response) {
					$scope.def = response.data;
				}
			);

			$http.get('api/lunch/add/' + $scope.id +'/').then(
				function(response) {
					$scope.add = response.data;
				}
			);

			$http.get('api/lunch/cancel/' + $scope.id +'/').then(
				function(response) {
					$scope.cancel = response.data;
				}
			);
		}
	}

	$scope.addDay = function() {
		$scope.addD.date = $filter('date')($scope.addD.date, 'yyyy-MM-dd');
		
		$http.post('api/lunch/add/' + $scope.id +'/', $scope.addD).then(
  			function(response) {
    			$scope.add.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  			}
  		);
	}

	$scope.cancelDay = function() {
		$scope.cancelD.date = $filter('date')($scope.cancelD.date, 'yyyy-MM-dd');
		
		$http.post('api/lunch/cancel/' + $scope.id +'/', $scope.cancelD).then(
  			function(response) {
    			$scope.cancel.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  			}
  		);
	}

	$scope.update = function() {
		$http.put('api/lunch/default/' + $scope.id +'/', $scope.def).then(
      		function(response) {
      			alert('Default Lunch Schedule has been updated!');
      		}
      	);
	}

	$scope.deleteDay = function(date, index, num) {
		$http.delete('api/lunch/exceptional/' +$scope.id +'/' + date +'/').then(
			function(response) {
				if (num==0)
					$scope.add.splice(index,1);
				else
					$scope.cancel.splice(index,1);
			}
		);
	}
});

app.controller('UserWorkingRegisterCtrl', function($rootScope, $http, $scope, $filter, $window) {
	$rootScope.hide = false;
	$scope.id = $window.localStorage.getItem('id');
	$scope.working = JSON.parse($window.localStorage.getItem('has_working_schedule'));
	$scope.login = $window.localStorage.getItem('login');

	if ($scope.login)
		$scope.username = $window.localStorage.getItem('username');
	else
		$scope.username = 'User';

	$rootScope.header = $scope.username + ' | Working Request';

	$scope.init = function() {

		if ($scope.login) {

			$http.get('api/working/default/'+$scope.id+'/').then(
				function(response) {
					$scope.def = response.data;
				}
			);

			$http.get('api/working/add/' + $scope.id +'/').then(
				function(response) {
					$scope.add = response.data;
				}
			);

			$http.get('api/working/cancel/' + $scope.id +'/').then(
				function(response) {
					$scope.cancel = response.data;
				}
			);
		}
	}

	$scope.addDay = function() {
		$scope.addD.date = $filter('date')($scope.addD.date, 'yyyy-MM-dd');
		
		$http.post('api/working/add/' + $scope.id +'/', $scope.addD).then(
  			function(response) {
    			$scope.add.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  			}
  		);
	}

	$scope.cancelDay = function() {
		$scope.cancelD.date = $filter('date')($scope.cancelD.date, 'yyyy-MM-dd');
		
		$http.post('api/working/cancel/' + $scope.id +'/', $scope.cancelD).then(
  			function(response) {
    			$scope.cancel.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  			}
  		);
	}

	$scope.update = function() {
		$http.put('api/working/default/' + $scope.id +'/', $scope.def).then(
      		function(response) {
      			alert('Default Lunch Schedule has been updated!');
      		}
      	);
	}

	$scope.deleteDay = function(date, index, num) {
		$http.delete('api/working/exceptional/' + $scope.id +'/' + date +'/').then(
			function(response) {
				if (num==0)
					$scope.add.splice(index,1);
				else
					$scope.cancel.splice(index,1);
			}
		);
	}
});

app.controller('UserLunchSummaryCtrl', function($rootScope, $scope, $http, $window, $state, $stateParams) {
	$rootScope.hide = false;
	$scope.id = $window.localStorage.getItem('id');
	$scope.login = $window.localStorage.getItem('login');
	$scope.working = JSON.parse($window.localStorage.getItem('has_working_schedule'));
	$scope.date = {};

	if ($scope.login)
		$scope.username = $window.localStorage.getItem('username');
	else
		$scope.username = 'User';

	$rootScope.header = $scope.username + ' | Lunch Summary';

	$scope.init = function() {

		if ($state.current.name == 'user_lunch_summary') {
			$http.get('api/lunch/personal/current/'+$scope.id+'/').then(
	  			function(response) {
			        $scope.sum = response.data;
			        $scope.arr = JSON.parse($scope.sum.calendar.calendar);
			        $scope.orderDays = $scope.sum.orderDays.split(',');
			        $scope.show = true;
	  			},
	  			function(response) {
	  				$scope.msg = 'Currently there is no month lunch summary!';
	  				$scope.show = false;
	  			}
			);
		}
		else if ($state.current.name == 'user_particular_lunch_summary') {
			$http.get('api/lunch/personal/'+$scope.id+'/'+$stateParams.year+'/'+$stateParams.month+'/').then(
	  			function(response) {
			        $scope.sum = response.data;
			        $scope.arr = JSON.parse($scope.sum.calendar.calendar);
			        $scope.orderDays = $scope.sum.orderDays.split(',');
			        $scope.show = true;
	  			},
	  			function(response) {
	  				$scope.msg = 'There is no month lunch summary in ' + $stateParams.year+'-'+$stateParams.month +'!';
	  				$scope.show = false;
	  			}
			);
		}
	}

	$scope.check = function() {
		$state.go('user_particular_lunch_summary', {year: $scope.date.year, month: $scope.date.month});
	}

	$scope.getCurrent = function() {
		$state.go('user_lunch_summary');
	}
});


app.controller('UserPersonalScheduleCtrl', function($rootScope, $scope, $http, $window, $state, range, $stateParams) {
	$rootScope.hide = false;
	$scope.id = $window.localStorage.getItem('id');
	$scope.working = JSON.parse($window.localStorage.getItem('has_working_schedule'));
	$scope.login = $window.localStorage.getItem('login');
	$scope.date = {};

	if ($scope.login)
		$scope.username = $window.localStorage.getItem('username');
	else
		$scope.username = 'User';

	$rootScope.header = $scope.username + ' | Personal Schedule';

	
	$scope.getCurrent = function(order) {
		if ($state.current.name == 'user_personal_schedule') {
			$scope.def = true;
			$http.get('api/working/personal/current/'+$scope.id+'/?order='+order).then(
	  			function(response) {
			        $scope.sum = response.data;
			        $scope.calendar = JSON.parse($scope.sum.calendar.calendar);
			        $scope.schedule = JSON.parse($scope.sum.personalSchedule);
			        $scope.show=true;
	  			},
	  			function(response) {
	  				$scope.show=false;
	  				if (order==0)
	  					$scope.msg = 'You currently have no working schedule!';
	  				else
	  					$scope.msg = 'You have no working schedule previously!';
	  			}
			);
		}
		else if ($state.current.name == 'user_particular_personal_schedule') {
			$scope.def = false;
			$http.get('api/working/personal/'+$scope.id+'/'+$stateParams.year+'/'+$stateParams.month+'/').then(
	  			function(response) {
			        $scope.sum = response.data;
			        $scope.calendar = JSON.parse($scope.sum.calendar.calendar);
			        $scope.schedule = JSON.parse($scope.sum.personalSchedule);
			        $scope.show=true;
	  			},
	  			function(response) {
	  				$scope.show=false;
	  				$scope.msg = 'You have no working schedule in '+ $stateParams.year+'-'+$stateParams.month+'!';
	  			}
			);
		}
	}

	$scope.back = function() {
		$state.go('user_personal_schedule');
	}

	$scope.init = function() {
		$scope.getCurrent(0);
	}

	$scope.check = function() {
		$state.go('user_particular_personal_schedule', {year: $scope.date.year, month: $scope.date.month});
	}

	$scope.range = function(start, stop, step) {
	    return range.getRange(start, stop, step);
	};
});

app.controller('UserSettingsCtrl', function($rootScope, $http, $scope, $filter, $window, $state) {
	$rootScope.hide = false;
	$scope.date_joined = $window.localStorage.getItem('date_joined');
	$scope.email = $window.localStorage.getItem('email');
    $scope.fullname = $window.localStorage.getItem('fullname');
    $scope.last_login = $window.localStorage.getItem('last_login');
    $scope.password = {};

	$scope.login = $window.localStorage.getItem('login');

	if ($scope.login)
		$scope.username = $window.localStorage.getItem('username');
	else
		$scope.username = 'User';

	$rootScope.header = $scope.username + ' | Settings';

	$scope.init = function() {
		$scope.date_joined = $filter('date')($scope.date_joined, 'yyyy-MM-dd');
	}

	$scope.reset = function() {
		$http.post('api/members/profile/reset_password/', $scope.password).then(
			function(response) {
				alert('Password has been successfully updated!');
				$state.go('logout');
			},
			function(response) {
				alert('Please check your password again!');
			}
		);
	}
});