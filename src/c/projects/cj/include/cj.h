/**
 * CJ.h - JavaScript-style Utility Header for C
 * 
 * Making C feel like JavaScript for modern developers
 * Because who doesn't want array.length in C? 🚀
 * 
 * Version: 1.0.0
 * License: MIT
 * Compatible: C99, C11+
 */

#ifndef CJ_H
#define CJ_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdarg.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ================================
 * BASIC UTILITIES (like JS basics)
 * ================================ */

// Get length of static array (like array.length)
#define len(arr) (sizeof(arr) / sizeof((arr)[0]))

// Math utilities (like Math.max, Math.min)
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
#define square(x) ((x) * (x))
#define cube(x) ((x) * (x) * (x))
#define abs_val(x) ((x) < 0 ? -(x) : (x))

// Swap utility (because JS has destructuring, we need this)
#define swap(a, b) do { \
    typeof(a) temp = (a); \
    (a) = (b); \
    (b) = temp; \
} while(0)

// Loop utilities (like for...of, while loops)
#define repeat(n) for(int _i = 0; _i < (n); _i++)
#define foreach(arr, len, action) \
    for(int _idx = 0; _idx < (len); _idx++) { \
        action((arr)[_idx], _idx); \
    }

/* ================================
 * DYNAMIC ARRAY UTILITIES
 * ================================ */

// Dynamic array structure (like JS arrays)
typedef struct {
    void *data;
    size_t length;
    size_t capacity;
    size_t element_size;
} cj_array_t;

// Create dynamic array (like new Array())
static inline cj_array_t* cj_array_new(size_t element_size) {
    cj_array_t *arr = malloc(sizeof(cj_array_t));
    if (!arr) return NULL;
    
    arr->data = malloc(element_size * 4); // Initial capacity of 4
    arr->length = 0;
    arr->capacity = 4;
    arr->element_size = element_size;
    return arr;
}

// Push to array (like array.push())
static inline bool cj_array_push(cj_array_t *arr, const void *element) {
    if (!arr || !element) return false;
    
    if (arr->length >= arr->capacity) {
        // Resize like JS engines do (roughly 1.5x growth)
        size_t new_capacity = arr->capacity * 2;
        void *new_data = realloc(arr->data, new_capacity * arr->element_size);
        if (!new_data) return false;
        
        arr->data = new_data;
        arr->capacity = new_capacity;
    }
    
    memcpy((char*)arr->data + (arr->length * arr->element_size), element, arr->element_size);
    arr->length++;
    return true;
}

// Pop from array (like array.pop())
static inline bool cj_array_pop(cj_array_t *arr, void *result) {
    if (!arr || arr->length == 0) return false;
    
    arr->length--;
    if (result) {
        memcpy(result, (char*)arr->data + (arr->length * arr->element_size), arr->element_size);
    }
    return true;
}

// Get element (like array[index])
static inline void* cj_array_get(cj_array_t *arr, size_t index) {
    if (!arr || index >= arr->length) return NULL;
    return (char*)arr->data + (index * arr->element_size);
}

// Free array (like setting to null)
static inline void cj_array_free(cj_array_t *arr) {
    if (arr) {
        free(arr->data);
        free(arr);
    }
}

// Convenience macros for typed arrays
#define ARRAY_NEW(type) cj_array_new(sizeof(type))
#define ARRAY_PUSH(arr, val) do { \
    typeof(val) _temp = (val); \
    cj_array_push((arr), &_temp); \
} while(0)
#define ARRAY_POP(arr, type) ({ \
    type _result; \
    cj_array_pop((arr), &_result) ? _result : (type){0}; \
})
#define ARRAY_GET(arr, index, type) (*(type*)cj_array_get((arr), (index)))

/* ================================
 * FUNCTIONAL PROGRAMMING (like JS)
 * ================================ */

// Map function (like array.map())
static inline cj_array_t* cj_array_map(cj_array_t *arr, void (*mapper)(const void*, void*)) {
    if (!arr || !mapper) return NULL;
    
    cj_array_t *result = cj_array_new(arr->element_size);
    if (!result) return NULL;
    
    for (size_t i = 0; i < arr->length; i++) {
        void *element = cj_array_get(arr, i);
        void *mapped = malloc(arr->element_size);
        mapper(element, mapped);
        cj_array_push(result, mapped);
        free(mapped);
    }
    
    return result;
}

// Filter function (like array.filter())
static inline cj_array_t* cj_array_filter(cj_array_t *arr, bool (*predicate)(const void*)) {
    if (!arr || !predicate) return NULL;
    
    cj_array_t *result = cj_array_new(arr->element_size);
    if (!result) return NULL;
    
    for (size_t i = 0; i < arr->length; i++) {
        void *element = cj_array_get(arr, i);
        if (predicate(element)) {
            cj_array_push(result, element);
        }
    }
    
    return result;
}

/* ================================
 * BIT MANIPULATION UTILITIES
 * ================================ */

#define bit_set(num, pos) ((num) |= (1ULL << (pos)))
#define bit_clear(num, pos) ((num) &= ~(1ULL << (pos)))
#define bit_toggle(num, pos) ((num) ^= (1ULL << (pos)))
#define bit_check(num, pos) (((num) >> (pos)) & 1ULL)

/* ================================
 * PRINT UTILITIES (like console.log)
 * ================================ */

// Generic print macro using _Generic (C11 feature)
#if __STDC_VERSION__ >= 201112L
#define print(x) _Generic((x), \
    int: printf("%d\n", x), \
    long: printf("%ld\n", x), \
    float: printf("%.2f\n", x), \
    double: printf("%.2f\n", x), \
    char*: printf("%s\n", x), \
    const char*: printf("%s\n", x), \
    char: printf("%c\n", x), \
    default: printf("Unknown type\n") \
)
#else
// C99 fallback - just print as pointer
#define print(x) printf("%p\n", (void*)&(x))
#endif

// Console-style logging
#define console_log(...) printf(__VA_ARGS__); printf("\n")
#define console_error(...) fprintf(stderr, __VA_ARGS__); fprintf(stderr, "\n")

/* ================================
 * STRING UTILITIES (like JS strings)
 * ================================ */

// String join (like array.join())
static inline char* cj_string_join(char **strings, size_t count, const char *separator) {
    if (!strings || count == 0) return NULL;
    
    size_t total_len = 0;
    size_t sep_len = separator ? strlen(separator) : 0;
    
    // Calculate total length
    for (size_t i = 0; i < count; i++) {
        if (strings[i]) total_len += strlen(strings[i]);
        if (i < count - 1) total_len += sep_len;
    }
    
    char *result = malloc(total_len + 1);
    if (!result) return NULL;
    
    result[0] = '\0';
    for (size_t i = 0; i < count; i++) {
        if (strings[i]) strcat(result, strings[i]);
        if (i < count - 1 && separator) strcat(result, separator);
    }
    
    return result;
}

// String repeat (like string.repeat())
static inline char* cj_string_repeat(const char *str, int times) {
    if (!str || times <= 0) return NULL;
    
    size_t len = strlen(str);
    char *result = malloc(len * times + 1);
    if (!result) return NULL;
    
    result[0] = '\0';
    for (int i = 0; i < times; i++) {
        strcat(result, str);
    }
    
    return result;
}

/* ================================
 * CONVENIENCE MACROS
 * ================================ */

// Boolean helpers (like JS truthy/falsy)
#define truthy(x) ((x) != 0 && (x) != NULL)
#define falsy(x) (!truthy(x))

// Null check (like JS optional chaining)
#define safe_access(ptr, member) ((ptr) ? (ptr)->member : 0)

// Memory helpers
#define new(type) ((type*)malloc(sizeof(type)))
#define new_array(type, count) ((type*)malloc(sizeof(type) * (count)))

// Debug helpers
#ifdef DEBUG
#define debug_print(...) printf("[DEBUG] " __VA_ARGS__); printf("\n")
#else
#define debug_print(...) ((void)0)
#endif

#ifdef __cplusplus
}
#endif

#endif /* CJ_H */