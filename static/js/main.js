(function () {
  'use strict';

  angular.module('BoggleApp', []).config(['$interpolateProvider', function($interpolateProvider) {
  		$interpolateProvider.startSymbol('{a');
  		$interpolateProvider.endSymbol('a}');
	}])
  .controller('BoggleController', ['$scope', '$log', '$http',
	function($scope, $log, $http) {
		$scope.nam = {
          a: 'Olgun'
        }		
	}
	]);
}());