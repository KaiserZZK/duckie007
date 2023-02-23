# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import gridworld

import random,util,math
import copy

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        "*** YOUR CODE HERE ***"
        self.values = util.Counter() # initialize the Q-value for each state-action pair to 0
        self.epsilon = args['epsilon']
        self.alpha = args['alpha']
        self.discount = args['gamma']

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        return self.values[(state, action)] # Counter() automatically outputs 0.0 for unseen states
        util.raiseNotDefined()

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        if len(self.getLegalActions(state)) == 0:
            return self.values[(state, None)]

        the_value = float('-inf')
        for a in self.getLegalActions(state):
            q_value = self.getQValue(state, a)  # >>>only access Q values by calling getQValue
            the_value = max(q_value, the_value)

        # print("the value from Q values is: ", the_value)
        return the_value
        util.raiseNotDefined()

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        '>>>choose an action from the starting/current state based on the current Q-values in the table<<<'
        'In a particular state, actions that your agent hasn’t seen before still have a Q-value, ' \
        'specifically a Q-value of zero, and if all of the actions that your agent has seen before ' \
        'have a negative Q-value, an unseen action may be optimal.<<<'
        '>>>which action brings the highest Q-value, based on the Q-values table?<<<'
        '>>>break ties randomly for better behavior, using random.choice() function' \

        '>>>only access Q values by calling getQValue<<<'
        if len(self.getLegalActions(state)) == 0:
            return []

        max_qvalue = float('-inf')
        the_action = None
        for a in self.getLegalActions(state):
            qval = self.getQValue(state, a)
            # print("qval %f VS. bestval %f" %(qval, max_qvalue))
            if max_qvalue == qval: # the trivial case where there is a tie
                the_action = random.choice([a, the_action]) # break ties by randomly choosing an action
            else:
                max_qvalue = max(qval, max_qvalue)
                if max_qvalue == qval:
                    the_action = a

        return the_action
        util.raiseNotDefined()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if len(legalActions) == 0:
            return action
        """def flipCoin(p):
            r = random.random()
            return r < p"""

        if util.flipCoin(self.epsilon): # if smaller than epsilon
            action = random.choice(legalActions)
        else:
            action = self.computeActionFromQValues(state)

        return action
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward: float):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        '>>>Q(s,a) <-- (1-alpha) * Q(s,a) + alpha * [R(s,a,s`) + gamma * max_action_Q(s`,a`)]<<<'

        current_q = self.getQValue(state, action)
        max_action_q = self.computeValueFromQValues(nextState)

        new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.discount * max_action_q)
        # print("aww geez, let's look at the stats... ", self.alpha, max_action_q, reward)
        self.values[(state, action)] = new_q
        # print("hon hon hon, I wonder whether the values have been properly updated? ", state, action, new_q)
        # util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)



class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent
       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        """class IdentityExtractor(FeatureExtractor):
            def getFeatures(self, state, action):
                feats = util.Counter()
                feats[(state, action)] = 1.0
                return feats""" # the IdentityExtractor assigns a single feature to every (state,action) pair.
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()
        self.values = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        '>>>Q(s,a) = w_1 * f_1(s,a) + w_2 * f_2(s,a) + ... + w_n * f_n(s,a)<<<'
        '>>> weights = {feature_name: function_weight, ...} <<<<'
        # if len(self.getLegalActions(state)) == 0:
        #     return 0
        features = self.featExtractor.getFeatures(state, action)
        the_q = 0
        # print("features active at this step?", state, features)

        for key in features:
            feature = features[key]
            weighted_state_q = feature * self.weights[key]
            # weighted_state_q = feature * self.weights[feature]
            the_q += weighted_state_q

        return the_q
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward: float):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"

        '>>> diff = ( r + gamma * max_action_Q(s`,a`) ) - Q(s,a) <<<'
        '>>> w_i = w_i + alpha * difference * f_i(s,a) <<<'

        features = self.featExtractor.getFeatures(state, action)

        current_q = self.getQValue(state, action)
        max_action_q = self.getValue(nextState)
        if len(self.getLegalActions(nextState)) == 0:
            diff = reward - current_q
        else:
            diff = reward + self.discount * max_action_q - current_q

        # self.values[(state, action)] = current_q + self.alpha * diff

        for key in features.keys():
            feature = features[key]
            current_weight = self.weights[key]
            new_weight = current_weight + self.alpha * diff * feature
            self.weights[key] = new_weight

        for key in self.values.keys():
            print(self.values[key])

    def final(self, state):
        """Called at the end of each game."""
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            print(self.values)
            pass
