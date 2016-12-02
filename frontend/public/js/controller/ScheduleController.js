app.controller('ScheduleCtrl', function($rootScope, $scope, $http, $window, $state, range, $stateParams) {
  $rootScope.hide = false;
  $scope.login = $window.localStorage.getItem('login');
  $scope.date = {};

	$scope.getCurrent = function(order) {

    if ($state.current.name == 'schedule') {
      $rootScope.header = 'Working Schedule';
      $scope.def = true;
      $http.get('api/working/schedule/current/?order='+order).then(
  			function(response) {
        	$scope.working = response.data;
          $scope.calendar = JSON.parse($scope.working.calendar.calendar);
          $scope.sche = JSON.parse($scope.working.schedule);
          $scope.show = true;
      	},
    		function(response) {
    			$scope.show = false;
          if (order==0)
            $scope.msg = "There is no working schedule currently!";
          else
            $scope.msg = "There is no working schedule previously!";
    		}
  		);
    }
    else if ($state.current.name == 'schedule_particular') {
      $rootScope.header = $stateParams.year+'-'+$stateParams.month + ' Working Schedule';
      $scope.def = false;
      $http.get('api/working/schedule/'+$stateParams.year+'/'+$stateParams.month+'/').then(
        function(response) {
          $scope.working = response.data;
          $scope.calendar = JSON.parse($scope.working.calendar.calendar);
          $scope.sche = JSON.parse($scope.working.schedule);
          $scope.show = true;
        },
        function(response) {
          $scope.show = false;
          $scope.msg = 'Working schedule in ' + $stateParams.year+'-'+$stateParams.month + ' does not exist!';
        }
      );
    }
	}

  $scope.init = function() {
    $scope.getCurrent(0);
  }

  $scope.range = function(start, stop, step) {
    return range.getRange(start, stop, step);
  };

	$scope.check = function() {
    $state.go('schedule_particular', {year: $scope.date.year, month: $scope.date.month});
  }

  $scope.back = function() {
    $state.go('schedule');
  }
});