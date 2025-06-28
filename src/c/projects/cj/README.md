# CJ.h - JavaScript-style Utility Header for C

**Making C feel like JavaScript for modern developers**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C Standard](https://img.shields.io/badge/C-C99%2FC11-blue.svg)](https://en.wikipedia.org/wiki/C11_(C_standard_revision))
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-green.svg)](https://github.com/yourusername/cj.h)

## Why CJ.h?

Tired of missing `array.length` in C? Want `console.log()` instead of `printf()`? Wish you had `array.push()` and `array.map()`? **CJ.h brings JavaScript-style utilities to C programming**, making it more approachable for modern developers while maintaining C's performance and control.

```c
#include "cj.h"

int main() {
    // JavaScript-style arrays
    cj_array_t *arr = ARRAY_NEW(int);
    ARRAY_PUSH(arr, 42);
    console_log("Array length: %zu", arr->length);
    
    // Functional programming
    cj_array_t *doubled = cj_array_map(arr, double_mapper);
    
    // Clean syntax
    repeat(5) {
        console_log("Hello, World!");
    }
    
    return 0;
}
```

## Quick Start

### Installation

1. Download cj.h from the include/ directory
2. Copy it to your project or system include path
3. Include it in your C files:

```c
#include "cj.h"
```

### Compilation

```bash
# C11 (recommended - enables generic print)
gcc -std=c11 -o myapp main.c

# C99 (compatible mode)
gcc -std=c99 -o myapp main.c

# With debug output
gcc -std=c11 -DDEBUG -o myapp main.c
```

## API Documentation

### Basic Utilities

| Function/Macro | Description | Example |
|----------------|-------------|---------|
| `len(arr)` | Get static array length | `len(numbers)` → 5 |
| `max(a, b)` | Maximum of two values | `max(10, 20)` → 20 |
| `min(a, b)` | Minimum of two values | `min(10, 20)` → 10 |
| `square(x)` | Square a number | `square(5)` → 25 |
| `swap(a, b)` | Swap two variables | `swap(x, y)` |

### Loop Utilities

```c
// Repeat n times (like for loop)
repeat(5) {
    printf("Hello! ");
}

// ForEach with index
int arr[] = {1, 2, 3};
foreach(arr, len(arr), print_with_index);
```

### Dynamic Arrays (JavaScript-style)

```c
// Create array
cj_array_t *arr = ARRAY_NEW(int);

// Push elements (like array.push())
ARRAY_PUSH(arr, 42);
ARRAY_PUSH(arr, 24);

// Access elements
int value = ARRAY_GET(arr, 0, int);

// Pop elements (like array.pop())
int last = ARRAY_POP(arr, int);

// Get length (like array.length)
size_t length = arr->length;

// Cleanup
cj_array_free(arr);
```

### Functional Programming

```c
// Map function (like array.map())
void double_int(const void *input, void *output) {
    *(int*)output = (*(int*)input) * 2;
}

cj_array_t *doubled = cj_array_map(original, double_int);

// Filter function (like array.filter())
bool is_positive(const void *input) {
    return *(int*)input > 0;
}

cj_array_t *positives = cj_array_filter(numbers, is_positive);
```

### String Utilities

```c
// Join strings (like array.join())
char *words[] = {"Hello", "World"};
char *result = cj_string_join(words, 2, " ");
// Result: "Hello World"

// Repeat strings (like string.repeat())
char *repeated = cj_string_repeat("Hi", 3);
// Result: "HiHiHi"
```

### Console & Logging

```c
// Console-style logging
console_log("Hello, %s!", "World");
console_error("Something went wrong!");

// Generic print (C11 only)
print(42);        // Prints: 42
print(3.14);      // Prints: 3.14
print("Hello");   // Prints: Hello

// Debug logging (only when DEBUG is defined)
debug_print("Debug info: %d", value);
```

### Bit Manipulation

```c
unsigned int flags = 0;

bit_set(flags, 2);      // Set bit 2
bit_clear(flags, 1);    // Clear bit 1
bit_toggle(flags, 3);   // Toggle bit 3
bool is_set = bit_check(flags, 2);  // Check if bit 2 is set
```

### Convenience Macros

```c
// Memory allocation
int *ptr = new(int);
int *arr = new_array(int, 10);

// Boolean helpers
if (truthy(value)) { /* ... */ }
if (falsy(pointer)) { /* ... */ }

// Safe access (null-safe)
int value = safe_access(struct_ptr, member);
```

## Project Structure

```
cj/
├── include/
│   └── cj.h              # Main header file
├── demo/
│   └── main.c            # Complete demo/example
├── README.md             # This file
└── LICENSE               # MIT License
```

## Compatibility

- **C Standards:** C99, C11+
- **Compilers:** GCC, Clang, MSVC
- **Platforms:** Linux, macOS, Windows, embedded systems
- **Dependencies:** Standard C library only

### Feature Compatibility

| Feature | C99 | C11+ |
|---------|-----|------|
| Basic utilities | ✅ | ✅ |
| Dynamic arrays | ✅ | ✅ |
| Functional programming | ✅ | ✅ |
| Generic print() | ❌ | ✅ |
| All other features | ✅ | ✅ |

## Future Roadmap

### Planned Modules

- `cj_string.h` - Advanced string manipulation
- `cj_array.h` - Extended array utilities
- `cj_math.h` - Mathematical functions
- `cj_async.h` - Async/Promise-like patterns
- `cj_json.h` - JSON parsing/serialization

### Development Features

- Unit tests with automated CI/CD
- Performance benchmarks
- Memory leak detection
- Static analysis integration
- Package manager support (vcpkg, Conan)

## Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/awesome-utility`
3. Make your changes and add tests
4. Submit a pull request

### Contribution Guidelines

- Follow existing code style and naming conventions
- Add comprehensive documentation and examples
- Ensure compatibility with both C99 and C11
- Include unit tests for new features
- Update README.md with new API documentation

## License

MIT License - see LICENSE file for details.

## Credits & Vision

CJ.h was created to bridge the gap between JavaScript's developer-friendly syntax and C's performance. Our vision is to make C programming more accessible to modern developers while maintaining the language's core strengths.

### Inspiration

- **Lodash** - Utility library philosophy
- **React** - Component-based thinking
- **Node.js** - Developer experience focus
- **Modern C++** - Template and macro techniques

### Core Team

Built with ❤️ by developers who love both JavaScript and C. Open source community contributions welcome!

---

Happy coding with CJ.h! 

**"Write C like JavaScript, run like C"**

---

## LICENSE

```text
MIT License

Copyright (c) 2025 CJ.h Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Quick Setup Commands

```bash
# Create the project structure
mkdir -p cj/include cj/demo

# Navigate to project
cd cj

# Copy files from above into respective directories

# Compile and run demo
gcc -std=c11 -o demo demo/main.c && ./demo

# Or with debug mode
gcc -std=c11 -DDEBUG -o demo demo/main.c && ./demo
```

## What You Get

✅ Complete header file (include/cj.h) - 300+ lines of production-ready C  
✅ Working demo (demo/main.c) - Shows every feature in action  
✅ Professional docs (README.md) - GitHub-ready documentation  
✅ MIT License - Open source friendly  
✅ Cross-platform - Works on Linux, macOS, Windows  
✅ Multiple C standards - C99 and C11 support  

Just copy each file into the right directory and start coding!