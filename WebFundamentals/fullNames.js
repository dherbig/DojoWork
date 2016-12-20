var students = [ 
     {first_name :  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

function fullNames(input){
	for (var objArr in input){
		console.log(students[objArr].first_name + " " + students[objArr].last_name);	
	}
}

fullNames(students);