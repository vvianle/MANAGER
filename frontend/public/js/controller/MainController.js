app.controller('MainCtrl', function($rootScope, $scope, $http, $window) {
	$rootScope.header = 'Welcome | MANAGER';
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.username = $window.localStorage.getItem('username');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.working = JSON.parse($window.localStorage.getItem('has_working_schedule'));
});

app.controller('HomeCtrl', function($rootScope, $scope, $http, $window){
  	$rootScope.header = 'Welcome | MANAGER';
  	$rootScope.hide = false;
});

app.controller('AuthCtrl', function($rootScope, $scope, $http, $window, $state, $timeout) {
	$rootScope.header = 'Login';
	$rootScope.hide = true;

	$scope.submit = function() {
		$http.post('api/login/', $scope.login).then (
			function(response) {
				$window.localStorage.clear();
				
				$scope.token = response.data.token;
				$window.localStorage.setItem('token', $scope.token);
				$window.localStorage.setItem('login', true);

			    $http.get('api/members/profile/', {headers: {'one-token': $scope.token}}).then(
				    function(response) {
				        $window.localStorage.setItem('id', response.data.id);
				        $window.localStorage.setItem('username', response.data.username);
				        $window.localStorage.setItem('is_admin', response.data.is_admin);
				        $window.localStorage.setItem('has_working_schedule', response.data.has_working_schedule);
				        $window.localStorage.setItem('date_joined', response.data.date_joined);
				        $window.localStorage.setItem('email', response.data.email);
				        $window.localStorage.setItem('fullname', response.data.fullname);
				        $window.localStorage.setItem('last_login', response.data.last_login);

				        $state.go('home');
				        $timeout(function() {
				        	$window.location.reload();
				        }, 25);
				    }
			   	);
			},
			function(response) {
				alert('Wrong password/email.');
			}
		);
	}

	$scope.logout = function() {
		$rootScope.header = 'Logout';
		$http.post('api/logout/').then(
			function(response) {
				$window.localStorage.clear(); 
			    $state.go('login');
			    $window.location.reload();
			},
			function(response) {
				$window.localStorage.clear();
				$state.go('login');
			}
		);
	}
});