(function(){
    "use strict";

      document.addEventListener('DOMContentLoaded', function(){

        var map = L.map('mapa').setView([-34.573016, -58.503973], 18);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        L.marker([-34.573016, -58.503973]).addTo(map)
            .bindPopup('Instituto Politecnico Modelo')
            .openPopup();

      }); //Contenido del DOM cargado
})()
