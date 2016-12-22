function shuffleAlt(arr){
	//Data Validation
	if(!Array.isArray(arr)){
		return "Error";
	}
	var holder = [];
	var new = [];
	//Repeat this a huge number of times
	for (var x = 0, x < Math.random()*37, x++){
		//Split the deck in half, convieninetly reversing the removed half
		for (var i = 0, i<Math.floor(arr.length()/2), i++){
			//We do split this in half rounded down, so we always know arr >= holder
			holder.push(arr.pop());
		}
		//Zip them together!
		for(var i=0, i<(arr.length()+holder.length()), i++){
			new.push(holder.pop());
			if (holder.length() != 0){
				new.push(holder.pop());
			}
		}
	}
	return new;	
}
