/**
 * CJ.h Demo - Showcasing JavaScript-style C programming
 * 
 * Compile with: gcc -std=c11 -o demo main.c
 * Or for C99: gcc -std=c99 -DDEBUG -o demo main.c
 */

#include "../include/cj.h"

// Example mapper function for array.map()
void double_int(const void *input, void *output) {
    *(int*)output = (*(int*)input) * 2;
}

// Example predicate for array.filter()
bool is_even(const void *input) {
    return (*(int*)input) % 2 == 0;
}

int main() {
    console_log("🚀 Welcome to CJ.h - JavaScript-style C programming!");
    console_log("===============================================");
    
    // ================================
    // Basic utilities demo
    // ================================
    console_log("\n📊 Basic Utilities:");
    
    int numbers[] = {1, 2, 3, 4, 5};
    console_log("Array length: %zu", len(numbers));
    console_log("Max of 10 and 20: %d", max(10, 20));
    console_log("Min of 10 and 20: %d", min(10, 20));
    console_log("Square of 7: %d", square(7));
    
    // Swap demo
    int a = 42, b = 24;
    console_log("Before swap: a=%d, b=%d", a, b);
    swap(a, b);
    console_log("After swap: a=%d, b=%d", a, b);
    
    // ================================
    // Loop utilities demo
    // ================================
    console_log("\n🔄 Loop Utilities:");
    
    printf("Repeat 5 times: ");
    repeat(5) {
        printf("★ ");
    }
    printf("\n");
    
    // ================================
    // Dynamic arrays demo
    // ================================
    console_log("\n📦 Dynamic Arrays (like JS arrays):");
    
    cj_array_t *arr = ARRAY_NEW(int);
    
    // Push elements (like array.push())
    ARRAY_PUSH(arr, 10);
    ARRAY_PUSH(arr, 20);
    ARRAY_PUSH(arr, 30);
    ARRAY_PUSH(arr, 40);
    ARRAY_PUSH(arr, 50);
    
    console_log("Array length after pushes: %zu", arr->length);
    
    // Access elements
    printf("Array contents: ");
    for (size_t i = 0; i < arr->length; i++) {
        printf("%d ", ARRAY_GET(arr, i, int));
    }
    printf("\n");
    
    // Pop element (like array.pop())
    int popped = ARRAY_POP(arr, int);
    console_log("Popped element: %d", popped);
    console_log("Array length after pop: %zu", arr->length);
    
    // ================================
    // Functional programming demo
    // ================================
    console_log("\n🎯 Functional Programming:");
    
    // Map demo (like array.map())
    cj_array_t *doubled = cj_array_map(arr, double_int);
    printf("Original: ");
    for (size_t i = 0; i < arr->length; i++) {
        printf("%d ", ARRAY_GET(arr, i, int));
    }
    printf("\nDoubled:  ");
    for (size_t i = 0; i < doubled->length; i++) {
        printf("%d ", ARRAY_GET(doubled, i, int));
    }
    printf("\n");
    
    // Filter demo (like array.filter())
    ARRAY_PUSH(arr, 15); // Add an odd number
    ARRAY_PUSH(arr, 22); // Add an even number
    
    cj_array_t *evens = cj_array_filter(arr, is_even);
    printf("All numbers: ");
    for (size_t i = 0; i < arr->length; i++) {
        printf("%d ", ARRAY_GET(arr, i, int));
    }
    printf("\nEven only:   ");
    for (size_t i = 0; i < evens->length; i++) {
        printf("%d ", ARRAY_GET(evens, i, int));
    }
    printf("\n");
    
    // ================================
    // Bit manipulation demo
    // ================================
    console_log("\n🔧 Bit Manipulation:");
    
    unsigned int flags = 0;
    bit_set(flags, 2);
    bit_set(flags, 5);
    console_log("After setting bits 2 and 5: %u", flags);
    console_log("Bit 2 is: %s", bit_check(flags, 2) ? "SET" : "CLEAR");
    console_log("Bit 3 is: %s", bit_check(flags, 3) ? "SET" : "CLEAR");
    
    bit_toggle(flags, 2);
    console_log("After toggling bit 2: %u", flags);
    
    // ================================
    // Print utilities demo (C11 only)
    // ================================
    #if __STDC_VERSION__ >= 201112L
    console_log("\n🖨️  Generic Print (C11):");
    print(42);
    print(3.14);
    print("Hello, CJ.h!");
    print('A');
    #endif
    
    // ================================
    // String utilities demo
    // ================================
    console_log("\n📝 String Utilities:");
    
    char *words[] = {"Hello", "JavaScript", "style", "C", "programming"};
    char *joined = cj_string_join(words, 5, " ");
    console_log("Joined string: %s", joined);
    
    char *repeated = cj_string_repeat("C", 5);
    console_log("Repeated 'C': %s", repeated);
    
    // ================================
    // Cleanup and finale
    // ================================
    console_log("\n🧹 Cleanup:");
    
    cj_array_free(arr);
    cj_array_free(doubled);
    cj_array_free(evens);
    free(joined);
    free(repeated);
    
    console_log("✅ All memory cleaned up!");
    console_log("\n🎉 CJ.h demo completed successfully!");
    console_log("Now you can write C like JavaScript! 🚀");
    
    return 0;
}