var map;
var newMarkersArray = [];
var oldMarkersArray = [];

function initialize() {

        var count = 0;
        var seconds = 3;

        var mapOptions = {
          center: new google.maps.LatLng(49.286083, -123.117117),
          zoom: 12
        };

        map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);


        getMarkerLocations();

        setInterval(function() {

            getMarkerLocations();
            count++;
            $('#counter').text(count);

        }, seconds*1000);




}

function getMarkerLocations(){

    $.getJSON($SCRIPT_ROOT + '/get_locs',{
        route: route,
        stop: stopNumber
//        allstops: allstops

    }, function(data) {

        console.log(data);
        console.log('-----');


        for(var i=0; i<newMarkersArray.length; i++){
            oldMarkersArray.push(newMarkersArray[i]);
        }

        newMarkersArray = []

        for (var i=0; i<data.locations.length; i++){
            addMarker(data.locations[i]);
        }

        for (var i=0; i<oldMarkersArray.length; i++){
            oldMarkersArray[i].setMap(null);
//            console.log('-');

        }

      });

      return false;

}

function addMarker(location) {

    var pos = new google.maps.LatLng(location[0], location[1]);
    var marker = new google.maps.Marker(
        {
            position: pos,
//            icon: {path: google.maps.SymbolPath.FORWARD_OPEN_ARROW, scale: 2},
            map: map

        });

    newMarkersArray.push(marker);
    marker.setMap(map);
}
