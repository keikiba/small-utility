
from transitions import Machine


class StateMachine:
    '''
    A simple example of state machine
    '''
    states = ['start', 's1', 's2', 'end']
    transitions = [
        {'trigger': 'go', 'source': 'start', 'dest': 's1', 'after': 'action_after'},
        {'trigger': 'go', 'source': 's1', 'dest': 's2', 'after': 'action_after'},
        {'trigger': 'go', 'source': 's2', 'dest': 'end', 'after': 'action_after'},

        {'trigger': 'back', 'source': 's1', 'dest': 'start', 'after': 'action_after'},
        {'trigger': 'back', 'source': 's2', 'dest': 's1', 'after': 'action_after'},

        # self transitions
        {'trigger': 'stay', 'source': ['start', 's1', 's2'],
        'dest': '=', 'after': 'action_after'},

        # internal transitions (= to invoke callback function without transition)
        {'trigger': 'print', 'source': '*', 'dest': None, 'before': 'action_before'},

        {'trigger': 'finish', 'source': ['start', 's1', 's2'], 'dest': 'end'}
    ]

    def __init__(self):
        self.initial_state = self.states[0]
        self.final_state = self.states[-1]
        self.machine = Machine(model=self,
                               states=self.states, initial=self.initial_state,
                               transitions=self.transitions, auto_transitions=False,
                               send_event=True,
                               prepare_event='action_prepare', finalize_event='action_finalize')

    def action_prepare(self, event):
        print(f'---')

    def action_before(self, event):
        print(f'action_before() called, state=[{event.state.name}]')

    def action_after(self, event):
        print(f'action_after() called, state=[{event.state.name}]')
    
    def action_finalize(self, event):
        evt = event.event.name
        src = event.transition.source
        dst = event.transition.dest
        print(f'transition: [{src}]-({evt})->[{dst}]')
        if self.state == self.final_state:
            print('completed')


def test_main():
    state_machine = StateMachine()
    for trg in ['go', 'go', 'back', 'stay', 'go', 'print', 'go']:
        state_machine.trigger(trg)
    pass

if __name__ == "__main__":
    test_main()
