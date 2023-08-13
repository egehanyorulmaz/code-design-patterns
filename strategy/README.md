# Strategy Pattern

The Strategy pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from the context that uses the algorithm. Below, you'll find an explanation of how this pattern works, its advantages and disadvantages, and its relevance in various scenarios.

## Introduction

The Strategy pattern provides a way to define a family of algorithms, encapsulate each one of them, and make them interchangeable. This pattern enables the algorithms to be selected at runtime without altering the code that uses them.

## How It Works

The Strategy pattern involves three key components: the Context, the Strategy, and Concrete Strategies. The Context delegates some behavior to a Strategy object. Concrete Strategies implement the algorithm defined by the Strategy interface.

## Benefits

Using the Strategy pattern offers several advantages:

1. **Encapsulates Algorithms:** Encapsulates related algorithms, allowing them to vary independently of the context.
2. **Promotes Open/Closed Principle:** Makes it easy to introduce new strategies without modifying existing code.
3. **Avoids Conditional Statements:** Reduces conditional complexity by moving conditional logic into strategy implementations.

## Disadvantages Compared to Other Patterns

However, it's essential to be aware of its limitations:

1. **Increased Number of Classes:** Introduces additional classes for each strategy, potentially adding complexity to the codebase.
2. **Context and Strategy Communication:** Must ensure proper communication between the context and the strategy, which can introduce additional complexity.

## Usage Example

You can use the Strategy pattern in systems where you need to choose from multiple algorithms to perform a specific operation, such as different sorting or payment methods.

## Applicability

Consider using the Strategy pattern when:
- You need to define a family of algorithms that are interchangeable.
- You want to hide complex or sensitive algorithmic details from the client.

## ChatGPT-generated Use Cases
| Case Name                 | Case Description                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------|
| Sorting Algorithms        | Allowing an application to choose from various sorting algorithms like quick sort, bubble sort, etc.                 |
| Payment Processing        | Handling different payment methods like credit card, PayPal, cryptocurrency.                                         |
| Compression Methods       | Managing various compression methods such as ZIP, RAR, TAR for file compression.                                     |
| Travel Route Planning     | Choosing different algorithms for travel route planning like shortest path, least cost, etc.                          |
| Image Rendering           | Selecting different image rendering algorithms based on the user's preferences or system capabilities.                 |

## Related Patterns

- **State Pattern**: Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.
- **Observer Pattern**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Resources

- [filter_strategy.py](filter_strategy.py) (See the [Credits](#credits) section for author information)

## Credits

This project makes use of code and resources from other authors. Full credit and appreciation go to the original creators:

- **filter_strategy.py:** Created by [NeetCode]("https://www.youtube.com/@NeetCode"), available at [Youtube](https://www.youtube.com/watch?v=tAuRQs_d9F8).

## References
* https://refactoring.guru/design-patterns/strategy

Please refer to the original sources for the applicable licenses and terms of use.
