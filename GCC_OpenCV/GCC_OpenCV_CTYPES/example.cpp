//example.cpp
#include <cstdint>

extern "C"{
	uint64_t calculateFactorial(uint64_t n){
	if(n == 0)
		return 1;
	else 
		return n * calculateFactorial(n - 1);
}

}
