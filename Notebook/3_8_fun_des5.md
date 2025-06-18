### Desafío 5

Crea una función llamada es_palindromo que tome una cadena y devuelva true si es palindromo o false si no lo es.

Solución dell ejercicio: 

Primero que nada, ¿Qué es un palindromo? un palindromo es es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, mayúsculas y tildes. como por ejemplo "somos" y "reconocer".

Ahora vamos con el código, el primer paso es definir la función: es_palindromo(cadena) que recibe una cadena de texto como parámetro, concepto de parámetro: dato o factor que se toma en cuenta para analizar o valorar una situación. Luego como segundo paso, dentro de la función: cadena.lower(), la utilizamos para que convierta todas las letras a minúscula para que no importe si está en mayúscula o no. Luego, continuanod en la misma línea usamos .replace(" ", "·), la cual elimina los espacios en blanco, ya que no afectan al palíndromo. Como tercer paso se compara la cadena original con su versión invertida, para invertirla usamos: cadena[::-1], esto no pone inicio ni fin, es decir, recorre toda la cadena y el -1 como paso significa: recorre hacia atras, por ende, como resultado devuelve una nueva cadena con los caracteres en orden inverso. Luego como cuarto paso para probar la función escribimos el texto que queremos probar si funciona, en nuestro caso utilizamos la palabra "reconocer", entonces quedaría así: texto = "reconocer", abajo ponemos resultado = es_palindromo(texto), y finalmente el print: print("¿Es palíndromo?", resultado), si el código está bien debería devolvernos en pantalla: True