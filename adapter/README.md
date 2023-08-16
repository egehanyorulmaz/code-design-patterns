# Adapter Pattern

The Adapter pattern is a structural design pattern used to allow incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces, making one class look like another class by providing a wrapper around it. Below, you'll find an explanation of how this pattern works, its advantages and disadvantages, and its relevance in various scenarios.

## Introduction

The Adapter pattern involves creating a new class (the adapter) that allows two existing classes with incompatible interfaces to work together. The adapter wraps one of the interfaces, converting its method calls into calls on the other interface.

## How It Works

The Adapter pattern includes the following components:
- **Target:** This is the interface that the client expects to work with.
- **Adapter:** This class makes a class with an incompatible interface compatible with the target interface.
- **Adaptee:** This is the existing class with an incompatible interface that needs to be adapted.

The adapter delegates the client's request to methods of the adaptee, converting the request to a form that the adaptee can understand.

## Benefits

Using the Adapter pattern offers several advantages:

1. **Increased Compatibility:** Allows two incompatible interfaces to work together, enhancing the reusability of existing code.
2. **Improved Maintainability:** By using adapters, you can change the behavior of a class without changing its code.
3. **Enhanced Flexibility:** Enables the integration of new features or third-party libraries that might have different interfaces.

## Disadvantages Compared to Other Patterns

However, it's essential to be aware of its limitations:

1. **Increased Complexity:** Introduces additional classes, which might add complexity to the codebase.
2. **Performance Overhead:** Additional layers of abstraction might lead to performance issues if not implemented carefully.

## Usage Example

You can use the Adapter pattern in the examples included below.

## Applicability

Consider using the Adapter pattern when:
- You want to use an existing class that has an interface that does not match the requirements of your system.
- You need to create a reusable class that cooperates with unrelated or unforeseen classes that don't necessarily have compatible interfaces.

## ChatGPT-generated Use Cases
| Case Name                          | Case Description                                                                                                                                          |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Legacy System Integration          | Enabling communication between new systems and legacy systems that may have different interfaces.                                                         |
| Third-party Library Integration    | Allowing integration of third-party libraries or APIs that might have different interfaces than expected.                                                 |
| Cross-platform Compatibility       | Making applications compatible across different platforms by using adapters to handle platform-specific functionality.                                    |
| Format Conversion                  | Converting data between different formats (e.g., XML to JSON) by providing an adapter that translates one format into another.                            |

## Related Patterns

- **Bridge Pattern**: Decouples an abstraction from its implementation, allowing the two to vary independently.
- **Decorator Pattern**: Adds new functionality to an object without altering its structure.

## Resources

- [usb_port.py](usb_port.py)

## Credits

This project makes use of code and resources from other authors. Full credit and appreciation go to the original creators:

## References
* https://refactoring.guru/design-patterns/adapter

Please refer to the original sources for the applicable licenses and terms of use.
