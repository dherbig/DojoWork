function time (hour, minute, period){
	var mn = PM;
	if (period==="AM"){
		mn = AM;
	}
	if (minute>30){
		console.log("It's almost "+hour+" in the "+mn)
	} else {
		console.log("It's just after "+hour+" in the "+mn)
	}
}