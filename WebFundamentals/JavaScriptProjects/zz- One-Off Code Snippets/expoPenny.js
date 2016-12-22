function expoPenny (){
	var total = 0;
	var day = 1;
	var amount = 0.01;
	while (day < 31){
		total = total + amount;
		amount *= 2;
		day++;
	}
	return total;
}

function expoPennyFor (days){
	var total;
	var amount;
	for (i=days, i>0, i++){
		total += amount;
		amount *= 2;
	}
}