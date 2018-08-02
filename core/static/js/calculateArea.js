/*Pega o canvas como referencia e cria uma variavel
contexto para serem feitas as operações*/
var canvas = document.getElementById('canvas')
var context = canvas.getContext('2d')

//variável flag como false para mostrar que não estamos calibrando a ferramenta
var flag = false

//função que seta a flag para true se o botão calibrar é clicado
document.getElementById('calibrate').onclick = function () { 
	flag = true
	return flag
}

/*função que pinta o interior da figura e calcula a area com base em pixels*/
function pintar(x, y){
	var cont = 0

	//vetor de movimento, movimenta em relação aos 4 vizinhos do pixel
	var movimentar_x = [1, -1, 0, 0]
	var movimentar_y = [0, 0, -1, 1]

	fila = [[x, y]]

	//loop de repetição, que passa pixel a pixel verificando se tem que ser pintado
	while(fila.length > 0){
		var r = fila[0][0]
		var s = fila[0][1]

		fila.shift()

		for (i = 0; i < 4; i++){

			xx = r + movimentar_x[i]
			yy = s + movimentar_y[i]

			var imgData = context.getImageData(xx, yy, 1, 1)

			//condicional para verificar se a cor do pixel é diferente da borda e da cor a ser pintada.
			//deconsiderando o canal alpha do padrão rgba
			if ((imgData.data[0] != 255 && imgData.data[1] != 0 && imgData.data[2] != 0) && (imgData.data[0] != 0 && imgData.data[1] != 0 && imgData.data[2] != 0)){
				cont++
			 	imgData.data[0] = 0
			 	imgData.data[1] = 0
			 	imgData.data[2] = 0
			 	imgData.data[3] = 255
			 	context.putImageData(imgData, xx, yy)
                fila.push([xx, yy])
			}
		}		 	 
	}
		/* se a flag for true ela atribui o contador para a variável escala
		que será usada posteriormente, se for false ela faz os calculos para retornar a 
		área da figura que se deseja calcular */
		if(flag == true){
			escala = cont
		}
		else{
			res = (parseFloat(cont)/parseFloat(escala))
			alert (res)
		}
		// setamos flag como falso novamete para que se possa fazer novos calculos
		flag = false
}

//funcão que pega as coordenadas x, y com o evento do mouse e passa como parametro para a função
function pegaPosicaoMouse(event) {
	var pos_x = event.offsetX
	var pos_y = event.offsetY
	// console.log("x coords: " + pos_x + ", y coords: " + pos_y);
	pintar(pos_x, pos_y)
	
}