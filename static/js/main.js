(function(){
    "use strict";

    var regalo = document.querySelector('#regalo');

    document.addEventListener('DOMContentLoaded', function(){
        /*
        var map = L.map('mapa').setView([-34.573016, -58.503973], 18);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        L.marker([-34.573016, -58.503973]).addTo(map)
            .bindPopup('Instituto Politecnico Modelo')
            .openPopup();

            */
        //Campos datos usuarios

        var nombre = document.querySelector('#nombre');
        var apellido = document.querySelector('#apellido');
        var email = document.querySelector('#email');


        //Campos Pases

        var paseDia = document.querySelector('#pase_dia');
        var paseDosDia = document.querySelector('#pase_dosdias');
        var paseCompleto = document.querySelector('#pase_completo');

        //Botones y divs
        var calcular = document.querySelector('#calcular');
        var errorDiv = document.querySelector('#error');
        var registro = document.querySelector('#btnRegistro');
        var lista_productos = document.querySelector('#lista-productos');
        var suma = document.querySelector('#suma-total');

        //Extras
        var camisas = document.querySelector('#camisa_evento');
        var etiquetas = document.querySelector('#etiquetas');

        calcular.addEventListener('click', calcularMontos);

        paseDia.addEventListener('blur', mostrarDias);
        paseDosDia.addEventListener('blur', mostrarDias);
        paseCompleto.addEventListener('blur', mostrarDias);

        nombre.addEventListener('blur', validarCampos);
        apellido.addEventListener('blur', validarCampos);
        email.addEventListener('blur', validarCampos);
        email.addEventListener('blur', validarMail);


        function validarCampos(){
            if(this.value == ''){
                errorDiv.style.display = 'block';
                errorDiv.innerHTML = "Este campo es obligatorio";
                this.style.border = "1px solid red";
                errorDiv.style.border = "1px solid red";
            }
            else{
                errorDiv.style.display = 'none';
                this.style.border = '1px solid #cccccc';
            }
        }

        function validarMail(){
            if(this.value.indexOf("@") > -1){
                errorDiv.style.display = 'none';
                this.style.border = '1px solid #cccccc';
            }
            else{
                errorDiv.style.display = 'block';
                errorDiv.innerHTML = "Este campo debe tener @";
                this.style.border = "1px solid red";
                errorDiv.style.border = "1px solid red";
            }
        }

        function calcularMontos(event){
            event.preventDefault();
            if(regalo.value === ''){
                alert("Debes elegir un regalo");
                regalo.focus();
            }
            else{
                console.log("Ya elegiste regalo");
                var boletoDia = parseInt(paseDia.value, 10)||0,
                    boletoDosDias = parseInt(paseDosDia.value, 10)||0,
                    boletoCompleto = parseInt(paseCompleto.value, 10)||0,
                    cantidadCamisas = parseInt(camisas.value, 10)||0,
                    cantidadEtiquetas =parseInt(etiquetas.value, 10)||0;

                var totalAPagar = (boletoDia * 30) + (boletoDosDias * 45) + (boletoCompleto * 50) + ((cantidadCamisas * 10) * .93) + (cantidadEtiquetas * 2);

                var listaProductos = [];

                if(boletoDia >= 1){
                    listaProductos.push(boletoDia + ' Pases por día');
                }
                if(boletoDosDias >= 1){
                    listaProductos.push(boletoDosDias + ' Pases por dos día');
                }
                if(boletoCompleto >= 1){
                    listaProductos.push(boletoCompleto + ' Pases completos');
                }
                if(cantidadCamisas >= 1){
                    listaProductos.push(cantidadCamisas + ' Camisas');
                }
                if(cantidadEtiquetas >= 1){
                    listaProductos.push(cantidadEtiquetas + ' Etiquetas');
                }

                lista_productos.style.display = 'block';
                lista_productos.innerHTML = '';
                for(var i = 0; i < listaProductos.length; i++){
                    lista_productos.innerHTML += listaProductos[i] + '<br>'
                }

                suma.innerHTML = '$ ' + totalAPagar.toFixed(2);
            }
        }

        function mostrarDias(){
            var boletoDia = parseInt(paseDia.value, 10)||0,
                boletoDosDias = parseInt(paseDosDia.value, 10)||0,
                boletoCompleto = parseInt(paseCompleto.value, 10)||0;

            var diasElegidos = [];

            if(boletoDia > 0){
                diasElegidos.push('#viernes');
            }
            if(boletoDosDias > 0){
                diasElegidos.push('#viernes', '#sabado');
            }
            if(boletoCompleto > 0){
                diasElegidos.push('#viernes', '#sabado', '#domingo');
            }

            for(var i = 0; i < diasElegidos.length; i++){
                document.querySelector(diasElegidos[i]).style.display = 'block';
            }

        }


    }); //Contenido del DOM cargado
})()
