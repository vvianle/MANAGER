app.controller('AdminUserLunchCtrl', function($rootScope, $scope, $http, $window) {
	$rootScope.header = 'Users Lunch Request';
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));

	$scope.getListUser = function() {
		$http.get('api/members/?filter=lunch').then(
			function(response) {
				$scope.users = response.data;
			}
		);
	}
});

app.controller('AdminMealPriceCtrl', function($rootScope, $scope, $filter, $http, $window) {
	$rootScope.hide = false;
	$rootScope.header = 'Update Meal Price';
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.price = {};

	$scope.init = function() {
		$http.get('api/lunch/mealprice/').then(
			function(response) {
				$scope.prices = response.data;
			}
		);
	}

	$scope.create = function() {
		$scope.price.startDate = $filter('date')($scope.price.startDate, 'yyyy-MM-dd');

		$http.post('api/lunch/mealprice/', $scope.price).then(
  			function(response) {
    			$scope.prices.push(response.data);
  			},
  			function(response) {
  				alert('This day already has a meal price available.');
  				$scope.price.price = "";
  				$scope.price.startDate = "";
  			}
  		);
	}

	$scope.delete = function(date, index) {
		$http.delete('api/lunch/mealprice/' + date +'/').then(
			function(response) {
				$scope.prices.splice(index,1);
			}
		);
	}
});

app.controller('AdminUserWorkingCtrl', function($rootScope, $scope, $http, $window) {
	$rootScope.header = 'Users Working Request';
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));

	$scope.getListUser = function() {
		$http.get('api/members/?filter=working').then(
			function(response) {
				$scope.users = response.data;
			}
		);
	}
});

app.controller('AdminSingleUserLunchCtrl', function($rootScope, $stateParams, $filter, $scope, $http, $location, $window) {
	$rootScope.header = 'Users Lunch Request';
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));

	$scope.init = function() {
		if ($scope.admin) {
			$http.get('api/lunch/default/' + $stateParams.id +'/').then(
				function(response) {
					$scope.def = response.data;
					$rootScope.header = response.data.user.username + ' Lunch Request';
				},
				function(response) {
					alert('That user does not exist!');
					$location.path('admin/users/lunch/')
				}
			);

			$http.get('api/lunch/add/' + $stateParams.id +'/').then(
				function(response) {
					$scope.add = response.data;
				}
			);

			$http.get('api/lunch/cancel/' + $stateParams.id +'/').then(
				function(response) {
					$scope.cancel = response.data;
				}
			);
		}
	}

	$scope.addDay = function() {
		$scope.addD.date = $filter('date')($scope.addD.date, 'yyyy-MM-dd');
		
		$http.post('api/lunch/add/' + $stateParams.id +'/', $scope.addD).then(
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
		
		$http.post('api/lunch/cancel/' + $stateParams.id +'/', $scope.cancelD).then(
  			function(response) {
    			$scope.cancel.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  			}
  		);
	}

	$scope.update = function() {
		$http.put('api/lunch/default/' + $stateParams.id +'/', $scope.def).then(
      		function(response) {
      			alert('Default Lunch Schedule has been updated!');
      		}
      	);
	}

	$scope.deleteDay = function(date, index, num) {
		$http.delete('api/lunch/exceptional/' +$stateParams.id +'/' + date +'/').then(
			function(response) {
				if (num==0)
					$scope.add.splice(index,1);
				else
					$scope.cancel.splice(index,1);
			}
		);
	}
});

app.controller('AdminSingleUserWorkingCtrl', function($rootScope, $stateParams, $filter, $scope, $http, $location, $window) {
	$rootScope.header = 'Users Working Request';
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));

	$scope.init = function() {
		if ($scope.admin) {
			$http.get('api/working/default/' + $stateParams.id +'/').then(
				function(response) {
					$scope.def = response.data;
					$rootScope.header = response.data.user.username + ' Working Request';
				},
				function(response) {
					alert('That user does not exist!');
					$location.path('admin/users/working/')
				}
			);

			$http.get('api/working/add/' + $stateParams.id +'/').then(
				function(response) {
					$scope.add = response.data;
				}
			);

			$http.get('api/working/cancel/' + $stateParams.id +'/').then(
				function(response) {
					$scope.cancel = response.data;
				}
			);
		}
	}

	$scope.addDay = function() {
		$scope.addD.date = $filter('date')($scope.addD.date, 'yyyy-MM-dd');
		
		$http.post('api/working/add/' + $stateParams.id +'/', $scope.addD).then(
  			function(response) {
    			$scope.add.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  				$scope.addD.date = "";
  			}
  		);
	}

	$scope.cancelDay = function() {
		$scope.cancelD.date = $filter('date')($scope.cancelD.date, 'yyyy-MM-dd');
		
		$http.post('api/working/cancel/' + $stateParams.id +'/', $scope.cancelD).then(
  			function(response) {
    			$scope.cancel.push(response.data);
  			},
  			function(response) {
  				alert('That day has already been added');
  				$scope.cancel.date = "";
  			}
  		);
	}

	$scope.update = function() {
		$http.put('api/working/default/' + $stateParams.id +'/', $scope.def).then(
      		function(response) {
      			alert('Default Working Schedule has been updated!');
      		}
      	);
	}

	$scope.deleteDay = function(date, index, num) {
		$http.delete('api/working/exceptional/' +$stateParams.id +'/' + date +'/').then(
			function(response) {
				if (num==0)
					$scope.add.splice(index,1);
				else
					$scope.cancel.splice(index,1);
			}
		);
	}
});

app.controller('AdminHolidayCtrl', function($rootScope, $scope, $http, $filter, $window) {
	$rootScope.hide = false;
  	$rootScope.header = 'Admin Holiday';
  	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.holiday = {};
	$scope.myHoliday = 'single';

  	$scope.init = function() {

	  	$http.get('api/holidays/').then(
			function(response) {
				$scope.holidays = response.data;
			}
		);
	}

	$scope.singleCreate = function() {
		$scope.clicked = true;

		if ($scope.holiday.noLunch || $scope.holiday.noWorking) {

			$scope.holiday.startDate = $filter('date')($scope.holiday.startDate, 'yyyy-MM-dd');
			$scope.holiday.endDate = $scope.holiday.startDate;

			$http.post('api/holidays/', $scope.holiday).then(
      			function(response) {
        			$scope.holidays.push(response.data);
        			$scope.clicked =false;
        			$scope.holiday.noWorking = false;
        			$scope.holiday.noLunch = false;
      			},
      			function(response) {
      				alert('Holiday has already been added');
      				$scope.clicked =false;
        			$scope.holiday.noWorking = false;
        			$scope.holiday.noLunch = false;
      			}
      		);
		}
	}

	$scope.rangeCreate = function() {
		$scope.clicked = true;

		if ($scope.holiday.noLunch || $scope.holiday.noWorking) {

			$scope.holiday.startDate = $filter('date')($scope.holiday.startDate, 'yyyy-MM-dd');
			$scope.holiday.endDate = $filter('date')($scope.holiday.endDate, 'yyyy-MM-dd');

			$http.post('api/holidays/', $scope.holiday).then(
      			function(response) {
        			$scope.holidays.push(response.data);
        			$scope.clicked =false;
        			$scope.holiday.noWorking = false;
        			$scope.holiday.noLunch = false;
      			},
      			function(response) {
      				alert('Holiday has already been added');
      				$scope.clicked =false;
        			$scope.holiday.noWorking = false;
        			$scope.holiday.noLunch = false;
      			}
      		);
		}
	}

	$scope.delete = function(pk, index) {
		$http.delete('api/holidays/' + pk +'/').then(
			function(response) {
				$scope.holidays.splice(index,1);
			}
		);
	}
});

app.controller('AdminUsersCreateCtrl', function($rootScope, $location, $scope, $http, $window, $state) {
	$rootScope.hide = false;
	$rootScope.header = 'Create User';
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.user = {};

	$scope.create = function() {
		$http.post('api/members/', $scope.user).then(
			function(response) {
				$scope.user = response.data;
				url = 'admin/users/';
				$location.path(url);
				$state.go('admin_users');
			},
			function(response) {
				alert('User cannot be created.');
				$state.reload();
			}
		);
	}
});

app.controller('AdminUsersCtrl', function($rootScope, $scope, $http, $window) {
	$rootScope.hide = false;
	$rootScope.header = 'Update Users';
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));

	$scope.init = function() {
		$http.get('api/members/').then(
			function(response) {
				$scope.members = response.data;
			}
		);
	}
});

app.controller('AdminUsersUpdateCtrl', function($rootScope, $stateParams, $scope, $http, $window, $state) {
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.username = $window.localStorage.getItem('username');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.user = {};

	$scope.init = function() {
		$http.get('api/members/' + $stateParams.id +'/').then(
			function(response) {
				$scope.user = response.data;
				$scope.n = $scope.user.username;
				$rootScope.header = "Update " + $scope.n;
			},
			function(response) {
				alert('That user does not exist!');
				$state.go('admin_users');
			}
		);
	}

	$scope.update = function() {
		$http.put('api/members/' + $stateParams.id +'/', $scope.user).then(
			function(response) {
				alert('User has been updated!');
				if ($scope.username == $scope.user.username) {
					if (($scope.user.password != null) && ($scope.user.password != ""))
						$state.go('logout');
					else
						$window.location.reload();
				}
				else
					$window.location.reload();
			},
			function(response) {
				alert('User cannot be updated!');
			}
		);
	}

	$scope.deactivate = function() {
		$http.delete('api/members/' + $stateParams.id +'/').then(
			function(response) {
				alert('User has been deactivate!');
				if ($scope.username == $scope.user.username)
					$state.go('logout');
				else
					$window.location.reload();
			}
		);
	}

	$scope.activate = function() {
		$scope.user.is_active = true;
		$http.put('api/members/' + $stateParams.id +'/', $scope.user).then(
			function(response) {
				alert('User has been activate!');
				$window.location.reload();
			}
		);
	}
});

app.controller('AdminScheduleCtrl', function($rootScope, $scope, $http, $window, range, $filter) {
	$rootScope.header = 'Update Schedule';
	$rootScope.hide = false;
	$scope.login = $window.localStorage.getItem('login');
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.today = $filter('date')(new Date(), 'yyyy-MM-dd');

	$scope.init = function(order) {
		$scope.option = [];
		$scope.msg = 'There is no schedule this month!';
		$http.get('api/working/schedule/current/?order='+order).then(
			function(response) {
				$scope.order = order;
				$scope.schedule_info = response.data;
				$scope.show = true;
				$scope.calendar = JSON.parse($scope.schedule_info.calendar.calendar);
				$scope.schedule = JSON.parse($scope.schedule_info.schedule);
				$scope.fix_schedule = angular.copy($scope.schedule);

				// get all active workers and workers in schedule when first generated
				$http.get('api/members/?filter=working').then(
					function(response) {
						$scope.users = response.data;

						for (var i=0; i < $scope.users.length; i++)
							$scope.option.push($scope.users[i].username);

						for (var i=0; i < $scope.schedule_info.users.length; i++) {
							if (!$scope.option.includes($scope.schedule_info.users[i]))
								$scope.option.push($scope.schedule_info.users[i]);
						}
						$scope.option.push('OPEN');
						$scope.option.push('Holiday');
					}
				);
				
				// separate workers working on Sunday
				for (var i=0; i < $scope.schedule.length; i++) {
					for (var x=0; x < $scope.schedule[i].length; x++) {
						if ($scope.schedule[i][x].includes(' | '))
							$scope.schedule[i][x] = $scope.schedule[i][x].split(' | ');
					}
				}
			},
			function(response) {
				$scope.show=false;
			}
		);
	}

	$scope.update = function() {
		$scope.schedule_info.schedule = JSON.parse(JSON.stringify($scope.schedule));
		for (var i=0; i < $scope.schedule_info.schedule.length; i++) {
			for (var x=0; x < $scope.schedule_info.schedule[i].length; x++) {
				if ((x==0) && ($scope.schedule_info.schedule[i][x]!=""))
					$scope.schedule_info.schedule[i][x] = $scope.schedule_info.schedule[i][x].join(' | ');
			}
		}
		$scope.schedule_info.schedule = JSON.stringify($scope.schedule_info.schedule);
		$http.put('api/working/schedule/current/?order='+$scope.order, $scope.schedule_info).then(
			function(response) {
				alert('Schedule has been updated!');
			}
		);
	}
	
	$scope.range = function(start, stop, step) {
		return range.getRange(start, stop, step);
	};
});


app.controller('AdminScheduleGenerateCtrl', function($rootScope, $scope, $http, $window, $state, range, $filter) {
	$rootScope.hide = false;
	$rootScope.header = 'Generate Schedule';
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.login = $window.localStorage.getItem('login');
	$scope.schedule = {};
	$scope.currentDay = $filter('date')(new Date(), 'yyyy-MM-dd');

	$scope.getCurrent = function(order) {
		
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

	$scope.generate = function() {
		$scope.schedule.startDate = $filter('date')($scope.schedule.startDate, 'yyyy-MM-dd');
		$http.post('api/working/generate/', $scope.schedule).then(
			function(response) {
				$state.go('schedule');
			}
		);
	}

	$scope.auto_generate = function() {
		$http.post('api/working/generate/').then(
			function(response) {
				$state.go('schedule');
			}
		);
	}

	$scope.range = function(start, stop, step) {
		return range.getRange(start, stop, step);
	};
});


app.controller('AdminLunchGenerateCtrl', function($rootScope, $scope, $http, $window, $state) {
	$rootScope.hide = false;
	$rootScope.header = 'Generate Lunch Request';
	$scope.admin = JSON.parse($window.localStorage.getItem('is_admin'));
	$scope.login = $window.localStorage.getItem('login');
	$scope.msg = 'There is no lunch order yet!';

	$scope.init = function() {
		$http.get('api/lunch/day/current/').then(
			function(response) {
	      		$scope.orders = response.data;
	        	$scope.show = true;
	    	},
	  		function(response) {
	  			$scope.show = false;
	  		}
		);
	}

	$scope.monthView = function() {
	    $scope.date = new Date($scope.orders.date);
	    $scope.month = $scope.date.getMonth()+1;
	    $scope.year = $scope.date.getFullYear();
	    $state.go('lunch_month_particular', {year: $scope.year, month: $scope.month});
	}

	$scope.generate = function() {
		$http.post('api/lunch/request/').then(
			function(response) {
				if (!("id" in response.data))
					alert('Today is a Holiday!!');
				else
					alert('Today Lunch Request has been successfully ordered!');
				$state.go('lunch_day');
			},
			function(response) {
				alert('Today Lunch Request has already been generated!');
				$state.go('lunch_day');
			}
		);
	}
});
