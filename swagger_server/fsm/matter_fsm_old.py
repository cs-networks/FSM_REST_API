""" FSM Model - Autogenerated by Loki - Code Gen
"""
#!/usr/bin/env python3

from transitions.extensions import GraphMachine as Machine
from transitions import MachineError
from transitions.extensions.markup import MarkupMachine

from swagger_server.models.action import Action  # noqa: E501

# The states
states = [
    { 'name': 'solid',
      'on_enter': [],
      'on_exit': [],
    }, 
    { 'name': 'liquid',
      'on_enter': [],
      'on_exit': [],
    }, 
    { 'name': 'gas',
      'on_enter': [],
      'on_exit': [],
    }, 
    { 'name': 'plasma',
      'on_enter': ['cb_on_enter_plasma'],
      'on_exit': ['cb_on_exit_plasma'],
    }
]

# And some transitions between states. We're lazy, so we'll leave out
# the inverse phase transitions (freezing, condensation, etc.).
transitions = [
    {  'trigger': 'melt', 
       'source': 'solid', 
       'dest': 'liquid', 
       'conditions': ['test1']
    },
    {  'trigger': 'freez', 
       'source': 'liquid', 
       'dest': 'solid', 
       'conditions': ['test2']
    },
    {  'trigger': 'evaporate', 
       'source': 'liquid', 
       'dest': 'gas', 
       'conditions': ['test3']
    },
    {  'trigger': 'condensate', 
       'source': 'gas', 
       'dest': 'liquid', 
       'conditions': ['test4']
    },
    {  'trigger': 'sublimate', 
       'source': 'solid', 
       'dest': 'gas', 
       'conditions': ['test5']
    },
    {  'trigger': 'deposit', 
       'source': 'gas', 
       'dest': 'solid', 
       'conditions': ['test6']
    },
    {  'trigger': 'ionize', 
       'source': 'gas', 
       'dest': 'plasma', 
       'conditions': ['test7']
    },
    {  'trigger': 'deionize', 
       'source': 'plasma', 
       'dest': 'gas', 
       'conditions': ['test8']
    }
]


class Matter():
    """Summary
    """
#####
# BEFORE_STATE_CHANGE Callbacks for FSM 
#####

    def cb_before_state_change(self):
        print("before_state_change Callback: cb_before_state_change")
        return True


#####
# AFTER_STATE_CHANGE Callbacks for FSM 
#####

    def cd_after_state_change(self):
        print("after_state_change Callback: cd_after_state_change")
        return True


    #####
    # Callbacks for transition melt
    #####

    def test1(self):
        print("Condition Callback: test1")
        return True


    #####
    # Callbacks for transition freez
    #####

    def test2(self):
        print("Condition Callback: test2")
        return True


    #####
    # Callbacks for transition evaporate
    #####

    def test3(self):
        print("Condition Callback: test3")
        return True


    #####
    # Callbacks for transition condensate
    #####

    def test4(self):
        print("Condition Callback: test4")
        return True


    #####
    # Callbacks for transition sublimate
    #####

    def test5(self):
        print("Condition Callback: test5")
        return True


    #####
    # Callbacks for transition deposit
    #####

    def test6(self):
        print("Condition Callback: test6")
        return True


    #####
    # Callbacks for transition ionize
    #####

    def test7(self):
        print("Condition Callback: test7")
        return True


    #####
    # Callbacks for transition deionize
    #####

    def test8(self):
        print("Condition Callback: test8")
        return True


    #####
    # On Enter Callbacks for state plasma
    #####

    def cb_on_enter_plasma(self):
        print("on_enter Callback: cb_on_enter_plasma")
        return True


    #####
    # On Exit Callbacks for state plasma
    #####
    def cb_on_exit_plasma(self):
        print("on_exit Callback: cb_on_exit_plasma")
        return True


class Hyper_MarkupMachine(MarkupMachine):
    def __init__(self, *args, **kwargs):
        """
        MarkupMachine extended with Hypermedia revelvant functions
        """
        MarkupMachine.__init__(self, *args, **kwargs)

    def get_current_state(self):
        return self.model.state

    def get_current_triggers(self):
        return self.get_triggers(self.get_current_state())

    def get_current_triggers_dict(self):
        trigger_list = []
        for trigger in self.get_triggers(self.get_current_state()):
            trigger_dict = {'trigger': trigger}
            trigger_list.append(trigger_dict)
        return trigger_list

    def get_actions_dict(self, id=''):
        actions = []
        for trigger in self.get_current_triggers_dict():
            new_action = Action(name=trigger['trigger'], 
                                title="transition", 
                                method="GET",
                                href="http://localhost:8763/v1/matter/" + str(id) + "/" + trigger['trigger'] )
            actions.append(new_action)
        return actions

    def state(self):
        return self.model.state


lump = Matter()

# Initialize
machine = Hyper_MarkupMachine(lump, 
                        states=states, 
                        transitions=transitions, 
                        initial='liquid',
                        before_state_change=['cb_before_state_change'],
                        after_state_change=['cd_after_state_change'],
                        ignore_invalid_triggers=True,
                        auto_transitions=False
                       )
