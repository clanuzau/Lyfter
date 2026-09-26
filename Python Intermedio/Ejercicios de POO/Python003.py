"""
Student: Cesar Lanuza Urbina
Program: This module defines classes to represent a human body and its parts.
"""


# Define classes for the human body parts and their connections.
class Head:
    """Represent the human's head."""

    pass

# Class Hand and Arm are defined to represent the human's hands and arms, respectively. Each arm is connected to a hand.
class Hand:
    """Represent one hand attached to an arm."""

    pass


# Class Arm is defined to represent the human's arms, which are connected to hands.
class Arm:
    def __init__(self, hand):
        """Connect the arm to its hand."""
        self.hand = hand


# Class Feet and Leg are defined to represent the human's feet and legs, respectively. Each leg is connected to a foot.
class Feet:
    """Represent one foot, using the class name required by the exercise."""

    pass 


# Class Leg is defined to represent the human's legs, which are connected to feet.
class Leg:
    def __init__(self, foot):
        """Connect the leg to its foot."""
        self.foot = foot


# Class Torso is defined to represent the human's torso, which connects the head, arms, and legs.
class Torso:
    # The constructor of the Torso class takes a head, two arms, and two legs as parameters and connects them to the torso.
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        """Connect the head, arms, and legs to the torso."""
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


# Class Human is defined to represent a human, which is built from a torso connected to all body parts.
class Human:
    def __init__(self, torso):
        """Build a human from a torso connected to all body parts."""
        self.torso = torso


# The following code creates a human by connecting all body parts through the torso and demonstrates 
# how to access nested attributes to verify the connections.
if __name__ == "__main__":
    # Create a separate hand for each arm.
    right_hand = Hand()
    left_hand = Hand()
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)

    # Create a separate foot for each leg.
    right_foot = Feet()
    left_foot = Feet()
    right_leg = Leg(right_foot)
    left_leg = Leg(left_foot)

    # Attach the head, both arms, and both legs to the torso.
    # Hands connect through the arms; feet connect through the legs.
    head = Head()
    torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
    # Compose the human from the torso and its connected body parts.
    human = Human(torso)

    # Access nested attributes to show how the body parts are connected.
    print()
    print("Torso connected:", human.torso is torso)
    print("Head connected:", human.torso.head is head)
    print("Right arm connected:", human.torso.right_arm is right_arm)
    print("Left arm connected:", human.torso.left_arm is left_arm)
    print("Right hand connected:", human.torso.right_arm.hand is right_hand)
    print("Left hand connected:", human.torso.left_arm.hand is left_hand)
    print("Right leg connected:", human.torso.right_leg is right_leg)
    print("Left leg connected:", human.torso.left_leg is left_leg)
    print("Right foot connected:", human.torso.right_leg.foot is right_foot)
    print("Left foot connected:", human.torso.left_leg.foot is left_foot)
    print("All body parts are connected correctly.")
    print()
