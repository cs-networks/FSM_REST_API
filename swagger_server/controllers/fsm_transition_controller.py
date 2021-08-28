""" FSM transition controller- Autogenerated by Loki - Code Gen
"""

import connexion
import six

from swagger_server import util

from swagger_server.database import db
from swagger_server.database.models.matter_model import matter_model
from swagger_server.fsm.matter_fsm import machine


def do_melt(matter_id):  # noqa: E501
    """Trigger transition melt

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'melt' in trigger_list:
            machine.model.melt()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_freez(matter_id):  # noqa: E501
    """Trigger transition freez

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'freez' in trigger_list:
            machine.model.freez()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_evaporate(matter_id):  # noqa: E501
    """Trigger transition evaporate

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'evaporate' in trigger_list:
            machine.model.evaporate()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_condensate(matter_id):  # noqa: E501
    """Trigger transition condensate

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'condensate' in trigger_list:
            machine.model.condensate()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_sublimate(matter_id):  # noqa: E501
    """Trigger transition sublimate

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'sublimate' in trigger_list:
            machine.model.sublimate()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_deposit(matter_id):  # noqa: E501
    """Trigger transition deposit

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'deposit' in trigger_list:
            machine.model.deposit()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_ionize(matter_id):  # noqa: E501
    """Trigger transition ionize

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'ionize' in trigger_list:
            machine.model.ionize()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


def do_deionize(matter_id):  # noqa: E501
    """Trigger transition deionize

    Advances the FSM # noqa: E501

    :param matter_id: The matter_id of the Matter object to retrieve
    :type matter_id: float

    :rtype: None
    """

    try: 
        model_obj = matter_model.get_by_id(id=matter_id)
        
        if model_obj is None:
            return "Matter object not found", 404

        fsm = model_obj.to_obj()

        machine.set_state(fsm.state)
        trigger_list = machine.get_current_triggers()
        if 'deionize' in trigger_list:
            machine.model.deionize()
            model_obj.state = machine.get_current_state()
            db.session.add(model_obj)
            db.session.commit()

            action_list = machine.get_actions_dict(id=fsm.id)
            self_link = Link( rel="self", href=f'http://localhost:8763/v1/matter/{fsm.id}')
        
            resp = MatterResponse(_class='matter', properties=fsm, actions=action_list, links=self_link)
            return resp            
        else:
            return "Transition not found", 404
    except:
        return "Internal Server Error", 500


