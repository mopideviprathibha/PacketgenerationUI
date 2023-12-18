var images = new Array() 
		images = [ "http://localhost/NPG/Images/Web-Dark.png", "http://localhost/NPG/Images/Web-Light.png"]; 

		setInterval("Animate()", 400); 
		var x = 0; 

		function Animate() { 
			document.getElementById("img").src = images[x] 
			x++; 
			if (images.length == x) { 
				x = 0; 
			} 
		} 