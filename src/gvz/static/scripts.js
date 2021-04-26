$('#searchtext').keypress(function (e) {
    var key = e.which;
    if(key == 13) {
        setUrl("search");
    }
});
function evalUrl () {
    console.log("evalUrl");
    var parts = window.location.pathname.split("/");
    if(parts[1] == "search") {
        search(parts[2]);
    }else if(parts[1] == "details"){
        details(parts[2]);
    }else{}
};
$(document).ready(function() {
    $("#searchbutton").click(function(){
        console.log("foo");
        setUrl("search");
    });
    evalUrl();
});
function setUrl(action, key) {
    if(action == "search") {
        key = $("#searchtext").val();
    }
    window.history.pushState("Foo", "Baz", "/"+action+"/"+key);
    evalUrl();
};

function search( term ) {
    $.get("/api/administrative_divisions/?search="+term, function(data, status){
        var searchhtml;
        $("#result").html("<p>Daten werden geladen, bitte warten ...</p>");
        searchhtml = "<h4 class='text-center'>Ergebnisse</h4><table class='table table-striped' style='width:100%;'>";
        searchhtml = searchhtml + "<thead><tr><th scope='col'>Ort</th><th>Typ</th><th>PLZ</th><th>Link</th></tr></thead>";
        for (item of data["results"]) {
            searchhtml = searchhtml + "<tr><td>"+item['name']+"</td><td>"+item['division_type_name']+"</td><td>"+item['zip_codes'].join(", ")+"</td><td><a href='/details/"+item['id']+"'>Details</a></td></tr>";
        };
        searchhtml = searchhtml + "</ul>";
        $("#result").html(searchhtml);
    });
};
function details( key ) {
    $("#result").html("<p>Daten werden geladen, bitte warten ...</p>");
    $.get("/api/administrative_divisions/"+key+"/", function(data, status){
        var searchhtml;
        searchhtml = "<table class='table table-striped' style='width:100%;'>" +
        "<thead><tr><th scope='col' colspan='2'><h4 class='text-center'>"+data['name']+"</h4></th></tr></thead>" +
        "<tr><th scope='row'>Gemeindeschl&uuml;ssel</th><td>"+data['ags']+"</td></tr>" +
        "<tr><th scope='row'>Gemeindetyp</th><td>"+data['division_type_name']+"</td></tr>" +
        "<tr><th scope='row'>Anschrift</th><td>"+data['office_name']+", "+data['office_street']+", "+data['office_city']+", "+data['office_zip']+"</td></tr>" +
        "<tr><th scope='row'>L&auml;ngengrad</th><td>"+data['longitude']+"</td></tr>" +
        "<tr><th scope='row'>Breitengrad</th><td>"+data['latitude']+"</td></tr>" +
        "<tr><th scope='row'>Bevölkerung gesamt</th><td>"+data['citizens_accumulated']["total"]+"</td></tr>" +
        "<tr><th scope='row'>Bevölkerung weiblich</th><td>"+data['citizens_accumulated']["female"]+"</td></tr>" +
        "<tr><th scope='row'>Bevölkerung männlich</th><td>"+data['citizens_accumulated']["male"]+"</td></tr>" +
        "<tr><th scope='row'>Fläche</th><td>"+data['area_accumulated']+"</td></tr>" +
        "<tr><th scope='row'>Übergeordnete Einheit</th><td><span id='parent-division'>wird berechnet...</span></td></tr>" +
        "<tr><th scope='row'>Untergeordnete Einheiten</th><td><span id='child-divisions'>wird berechnet...</span></td></tr>" +
        "<tr><th scope='row'>Postleitzahlen</th><td>"+data['zip_codes'].join(', ')+"</td></tr>" +
        "</table>";
        $("#result").html(searchhtml);
        get_parent(data["parent"]);
        get_children(data["id"]);
    });
}

function get_parent( url ) {
    $.get(url, function(data, status){
        $("#parent-division").html("<a href='/details/"+data["id"]+"'>"+data["name"]+" ("+data["division_type_name"]+")</a>");
    });
}

function get_children( parent_id ) {
    $.get("/api/administrative_divisions/?parent="+parent_id, function(data, status){
        if(data["count"] == 0) { $("#child-divisions").html("keine"); }
        var children_list = "";
        for (item of data["results"]) {
            children_list = children_list + "<a href='/details/"+item["id"]+"'>"+item["name"]+" ("+item["division_type_name"]+")</a><br>";
        }
        $("#child-divisions").html(children_list);
    });
}
