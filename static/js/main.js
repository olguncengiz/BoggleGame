(function () {
  'use strict';

  angular.module('BoggleApp', []).config(['$interpolateProvider', function($interpolateProvider) {
  		$interpolateProvider.startSymbol('{a');
  		$interpolateProvider.endSymbol('a}');
	}])
  .controller('BoggleController', ['$scope', '$log', '$http',
	function($scope, $log, $http) {
    $scope.letters = [];
    $scope.validity = "";

    $scope.getLetters = function() {
      $scope.status = "Shuffling";
      
      $log.log("Inside getLetters Function");

      $http({
        url: '/shuffle',
        dataType: 'json',
        method: 'GET',
        //params: {"galleryId": galleryId},
        headers: {
          "Content-Type": "application/json"
        }
      }).success(function(response){
        $log.log(response);
        if(response)
        {
          $scope.letters = response;
          $scope.status = "";
        }
        else
        {
          $scope.status = response.message;
        }
      }).error(function(error){
        $log.log(error);
        $scope.status = "Error Retrieving Letters, Please Try Again...";
      });
    };

    $scope.checkWord = function() {
      var tWord;
      $scope.status = "Checking...";
      tWord = $scope.word;

      tWord = tWord.replace(/i/g, "İ");
      tWord = tWord.replace(/ı/g, "I");

      tWord = tWord.toUpperCase();
      
      $log.log("Inside checkWord Function");

      $http({
        url: '/checkWord/' + tWord,
        dataType: 'json',
        method: 'GET',
        //params: {"word": word},
        headers: {
          "Content-Type": "application/json"
        }
      }).success(function(response){
        $log.log(response);
        if(response)
        {
          $scope.validity = tWord + ":" + response + $scope.validity;
          $log.log(tWord + ":" + response);
          $scope.status = "";
        }
        else
        {
          $scope.status = response.message;
        }
      }).error(function(error){
        $log.log(error);
        $scope.status = "Error Checking Word, Please Try Again...";
      });
      $scope.word = "";
    };
	}
	]);
}());