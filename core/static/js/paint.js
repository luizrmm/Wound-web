var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
context.lineWidth = 2;
context.strokeStyle = "#FF0000";
var down = false;
context.fillStyle="#FF0000";
////////////////////////////////////////////////

rect = {},
drag = false;

function draw() {
  context.fillRect(rect.startX, rect.startY, rect.w, rect.h);
}

function mouseDown(e) {
  rect.startX = e.pageX - this.offsetLeft;
  rect.startY = e.pageY - this.offsetTop;
  drag = true;
}

function mouseUp() {
  drag = false;
}

function mouseMove(e) {
  if (drag) {
    rect.w = (e.pageX - this.offsetLeft) - rect.startX;
    rect.h = (e.pageY - this.offsetTop) - rect.startY ;
    //context.clearRect(0,0,canvas.width,canvas.height);
    draw();
  }
}

function init() {
  canvas.addEventListener('mousedown', mouseDown, false);
  canvas.addEventListener('mouseup', mouseUp, false);
  canvas.addEventListener('mousemove', mouseMove, false);
}
init();

///////////////////////////////////////////////
function start(){

  	canvas.removeEventListener('mousedown', mouseDown, false);
  	canvas.removeEventListener('mouseup', mouseUp, false);
  	canvas.removeEventListener('mousemove', mouseMove, false);

	canvas.addEventListener('mousemove', draw);

	canvas.addEventListener('mousedown', function()
	{
		down = true;
		context.beginPath();
		context.moveTo(xPos, yPos);
		canvas.addEventListener("mousemove", draw);
	});

	canvas.addEventListener('mouseup', function(){ down = false; });

	function draw(e)
	{
		xPos = e.offsetX;
		yPos = e.offsetY;

		if(down == true)
		{	
			context.lineTo(xPos, yPos);
			context.stroke();
		}

	}
}

function clearCanvas() { context.clearRect(0, 0, canvas.width, canvas.height); }
function triggerClick() { document.getElementById('file').click(); }

document.getElementById('file').addEventListener('change', function(e)
{
	clearCanvas();
	var temp = URL.createObjectURL(e.target.files[0]);
	var image = new Image();
	image.src = temp;
	console.log(image)

	image.addEventListener('load', function()
	{
		imageWidth = image.naturalWidth;
		imageHeight = image.naturalHeight;
		newImageWidth = imageWidth;
		newImageHeight = imageHeight;
		originalImageRatio = imageWidth / imageHeight;

		if(newImageWidth > newImageHeight && newImageWidth > 800)
		{
			newImageWidth = 800;
			newImageHeight = 800 / originalImageRatio;
		}

		if(newImageWidth > newImageHeight && newImageHeight > 500)
		{
			newImageHeight = 500;
			newImageWidth = 500 * originalImageRatio;
		}

		if(newImageHeight > newImageWidth && newImageHeight > 500)
		{
			newImageHeight = 500;
			newImageWidth = 500 * originalImageRatio;
		}

		if(newImageWidth == newImageHeight && newImageHeight > 500)
		{
			newImageHeight = 500;
			newImageWidth = 500;
		}


		context.drawImage(image, 0, 0, newImageWidth, newImageHeight);
		URL.revokeObjectURL(temp);
	});
});