from abc import abstractmethod


class TrafficLightState:
    @abstractmethod
    def switch(self, light):
        pass


# states of the traffic light
class RedState(TrafficLightState):
    def switch(self, light):
        print("Red light - stop!")
        light.state = YellowState()
        light.previous_state = 'red'


class YellowState(TrafficLightState):
    def switch(self, light):
        if light.previous_state == 'red':
            print("Yellow light - prepare to go!")
            light.state = GreenState()

        elif light.previous_state == 'green':
            print("Yellow light - prepare to stop!")
            light.state = RedState()


class GreenState(TrafficLightState):
    def switch(self, light):
        print("Green light - go!")
        light.state = YellowState()
        light.previous_state = 'green'


# controls the logic of the traffic light
class TrafficLight:
    def __init__(self):
        self.state = RedState()
        self.previous_state = None

    def change(self):
        self.state.switch(self)


# Example usage
light = TrafficLight()
for _ in range(10):
    light.change()
