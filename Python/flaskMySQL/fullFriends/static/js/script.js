
alert("I'm Here!")
function submitform(id){
  // if(document.pressed == 'Edit')
  // {
  //  document.myform.action ="insert.html";
  // }
  // else
  // if(document.pressed == 'Delete')
  // {
  //   document.myform.action ="update.html";
  // }

	document.this.action = '/friends/' + id + document.pressed
	alert(document.this.action);
	console.log(document.pressed);
  return document.this.action;
}
