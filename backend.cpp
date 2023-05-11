#include <iostream>
#include <vector>

//когда изменен backend.cpp обязательно прописывать команду ниже в терминале!!!
//g++ -fPIC -shared -o backend.so backend.cpp

extern "C"{

	int hod = 0, n = 3;
	char v[3][3] = {{'-','-','-'},{'-','-','-'},{'-','-','-'}};

	int paintRect(int field){
		if (hod == 0) 
		{
			if (field % 3 == 0) v[(field-1)/3][2] = 'x';
			if (field % 3 == 1) v[(field-1)/3][0] = 'x';
			if (field % 3 == 2) v[(field-1)/3][1] = 'x';
			hod = 1;
			return 0; 
		}else 
		{
			if (field % 3 == 0) v[(field-1)/3][2] = 'o';
			if (field % 3 == 1) v[(field-1)/3][0] = 'o';
			if (field % 3 == 2) v[(field-1)/3][1] = 'o';
			hod = 0;
			return 1; 
		}
	}

	int getHod(){
		return hod;
	}

	void restartGame(){
		v[0][0] = '-';
	    v[0][1] = '-';
	    v[0][2] = '-';
	    v[1][0] = '-';
	    v[1][1] = '-';
	    v[1][2] = '-';
	    v[2][0] = '-';
	    v[2][1] = '-';
	    v[2][2] = '-';
	    v[3][0] = '-';
	    v[3][1] = '-';
	    v[3][2] = '-';
	    hod = 0;
	}

	int isGameOver(){
		for (int i = 0; i < n; i++) {
      		// Check rows
	      	if (v[i][0] != '-' && v[i][0] == v[i][1] && v[i][1] == v[i][2]) {
	        	return 1;
	      	}
	      	// Check columns
	      	if (v[0][i] != '-' && v[0][i] == v[1][i] && v[1][i] == v[2][i]) {
	        	return 1;
	      	}
    	}
	    // Check diagonals
	    if (v[0][0] != '-' && v[0][0] == v[1][1] && v[1][1] == v[2][2]) {
	      	return 1;
	    }
	    if (v[0][2] != '-' && v[0][2] == v[1][1] && v[1][1] == v[2][0]) {
	      	return 1;
	    }

	    // Check for a tie
	    for (int i = 0; i < n; i++) {
	      	for (int j = 0; j < n; j++) {
	        	if (v[i][j] == '-') {
	          		return 0;
	        	}
	      	}
	    }

	    // If we get here, it's a tie
	    return 2;
	}

}