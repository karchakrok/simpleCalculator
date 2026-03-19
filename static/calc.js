function valeur(x) {
	document.getElementById('resultat').value += x;
}

function effacer(y) {
    document.getElementById('resultat').value = y;
}

function calculer() {
	var result = eval(document.getElementById('resultat').value);
	document.getElementById('resultat').value = result;
}