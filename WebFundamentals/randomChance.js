function randomChance(quart){
	var bank = quart;
	var attempt = 1;
	while (bank>0){
		bank--;
		var result = Math.floor(Math.random()*100);
		if (result === 0){
			bank =+ Math.floor(Math.random()*50 + 50);
			attempt++;
			return bank;
		}else {		
			attempt++;
		}	
	}
	return 0;
}