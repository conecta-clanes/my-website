export class StateMachine {
  constructor(context, name) {
    this.context = context;
    this.name = name ?? 'fsm';
    this.states = new Map();
    this.currentState = null;
    this.previousState = null;
    this.isTransitioning = false;
  }

  addState(name, config = {}) {
    this.states.set(name, {
      name,
      onEnter: config.onEnter?.bind(this.context),
      onUpdate: config.onUpdate?.bind(this.context),
      onExit: config.onExit?.bind(this.context),
    });
    return this;
  }

  setState(name) {
    if (!this.states.has(name)) {
      console.warn(`[StateMachine:${this.name}] Unknown state: ${name}`);
      return this;
    }
    if (this.isTransitioning) return this;
    if (this.currentState?.name === name) return this;

    this.isTransitioning = true;
    this.previousState = this.currentState;
    this.currentState?.onExit?.();
    this.currentState = this.states.get(name);
    this.currentState.onEnter?.();
    this.isTransitioning = false;
    return this;
  }

  update(dt) {
    this.currentState?.onUpdate?.(dt);
  }

  is(name) { return this.currentState?.name === name; }
  was(name) { return this.previousState?.name === name; }
  getState() { return this.currentState?.name; }
}
