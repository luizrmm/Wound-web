var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
context.lineWidth = 2;
var down = false;

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

function changeColor(color) { context.strokeStyle = color; }
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