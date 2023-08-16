# Design Patterns

Design Patterns are general reusable solutions to common problems encountered in software design. They are not blueprints but guidelines to follow or customize according to the needs of the individual application. This document highlights three main categories of design patterns: Creational, Behavioral, and Structural patterns.

## Creational Patterns

Creational design patterns are concerned with the process of object creation, making a system independent of how its objects are created, composed, and represented.

### Examples
- **Singleton Pattern:** Ensures a class has only one instance and provides a global point to access it.
- **Factory Pattern:** Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
- **Builder Pattern:** Allows the construction of a complex object step by step. It's especially useful when an object needs to be created with many possible configurations.

## Behavioral Patterns

Behavioral design patterns are concerned with the responsibility and interaction between objects, promoting loose coupling and flexibility.

### Examples
- **Observer Pattern:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated. Commonly known as the Publish-Subscribe pattern.
- **Strategy Pattern:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- **State Pattern**: Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Structural Patterns

Structural design patterns are concerned with the composition of classes or objects, defining ways to compose objects to obtain new functionality.

### Examples
- **Adapter Pattern:** Allows the interface of an existing class to be used as another interface.
- **Composite Pattern:** Composes objects into tree structures to represent part-whole hierarchies.

## Comparison of Patterns

- **Creational Patterns:**
  - Focus: Object Creation
  - Complexity: Varies
  - Flexibility: High in object construction
  - Use Case: When the creation process should be decoupled from the system

- **Behavioral Patterns:**
  - Focus: Object Collaboration
  - Complexity: Can be complex due to relationships
  - Flexibility: High in object responsibilities and collaboration
  - Use Case: When objects have well-defined roles and relationships

- **Structural Patterns:**
  - Focus: Object Composition
  - Complexity: Varies
  - Flexibility: High in defining new compositions
  - Use Case: When designing how objects and classes interact or build on one another

## Conclusion

Design patterns offer valuable insights into designing flexible, clean, and maintainable code. Understanding the differences and similarities between Creational, Behavioral, and Structural patterns can guide developers in choosing the right pattern for their specific needs and scenarios.

## Resources
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612) by Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
- [Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Brain-Friendly/dp/0596007124) by Eric Freeman, Bert Bates, Kathy Sierra, Elisabeth Robson
- [RefactoringGuru - Design Patterns](https://refactoring.guru/design-patterns)

## Credits

This document draws on various resources, methodologies, and contributions from the software design community. Full credit and appreciation go to the original creators of these design patterns.
