app.controller('LunchDayCtrl', function($rootScope, $scope, $http, $window, $filter, $state, $stateParams) {
  $rootScope.hide = false;
  $scope.login = $window.localStorage.getItem('login');
  $scope.day = {};

	$scope.init = function() {
    $rootScope.header = 'Daily Lunch Order';
    if ($state.current.name == 'lunch_day') {
  		$http.get('api/lunch/day/current/').then(
  			function(response) {
        	$scope.orders = response.data;
          $scope.show = true;
      	},
    		function(response) {
    			$scope.show = false;
          $scope.msg = 'There is no lunch order yet!';
    		}
  		);
    }
    else if ($state.current.name == 'lunch_day_particular') {
      $rootScope.header = $stateParams.date+ ' Lunch Order';
      $http.get('api/lunch/day/' + $stateParams.date +'/').then(
        function(response) {
          $scope.orders = response.data;
          $scope.show = true;
        },
        function(response) {
          $scope.show = false;
          $scope.msg = 'There is no lunch order on ' + $stateParams.date +'!';
        }
      );
    }
	}

  $scope.getCurrent = function() {
    $state.go('lunch_day');
  }

	$scope.check = function() {
    $scope.date = $filter('date')($scope.day.date, 'yyyy-MM-dd');
    $state.go('lunch_day_particular', {'date': $scope.date});
	}

  $scope.monthView = function() {
    $scope.date = new Date($scope.orders.date);
    $scope.month = $scope.date.getMonth()+1;
    $scope.year = $scope.date.getFullYear();
    $state.go('lunch_month_particular', {year: $scope.year, month: $scope.month});
  }
});


app.controller('LunchMonthCtrl', function($rootScope, $scope, $http, $window, $state, $stateParams){
  $rootScope.hide = false;
  $scope.login = $window.localStorage.getItem('login');
  $scope.date = {};

  $scope.init = function() {
    $rootScope.header = 'Lunch Order Summary';
    
    if ($state.current.name == 'lunch_month') {
      $http.get('api/lunch/month/current/').then(
        function(response) {
          $scope.sums = response.data;
          $scope.msg = 'Currently there is no month lunch summary!';
          if ($scope.sums.length > 0) {
            $scope.arr = JSON.parse($scope.sums[0].calendar.calendar).toString().split(',');
          
            for (var sum=0; sum < $scope.sums.length; sum++)
              $scope.sums[sum].orderDays = $scope.sums[sum].orderDays.split(',');
          }
        }
      );
    }
    else if ($state.current.name == 'lunch_month_particular') {
      $rootScope.header = $stateParams.year+'-'+$stateParams.month + ' Lunch Order Summary ';

      $http.get('api/lunch/month/'+$stateParams.year+'/'+$stateParams.month+'/').then(
        function(response) {
          $scope.sums = response.data;
          $scope.msg = 'There is no lunch summary in ' + $stateParams.year+'-'+$stateParams.month + '!';
          if ($scope.sums.length > 0) {
            $scope.arr = JSON.parse($scope.sums[0].calendar.calendar).toString().split(',');
          
            for (var sum=0; sum < $scope.sums.length; sum++)
              $scope.sums[sum].orderDays = $scope.sums[sum].orderDays.split(',');
          }
        }
      );
    }
  }
  $scope.getCurrent = function() {
    $state.go('lunch_month');
  }
  $scope.check = function() {
    $state.go('lunch_month_particular', {'year': $scope.date.year, 'month': $scope.date.month});
  }
});
