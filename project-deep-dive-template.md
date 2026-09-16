# Project deep dive: [project name]

Fill one of these for each of 2 or 3 projects. Pick projects that cover different ground: one with deep technical design, one with cross-team scope, and one where something went wrong and you recovered. Generalize anything confidential (use "a payments service at ~50k QPS" instead of internal names).

**One-line summary:** What it is, your role, the scale, and the outcome.

---

## 1. Context

- **Problem:** What was broken or missing, and what it cost (in numbers: incidents, latency, dollars, engineer time).
- **Constraints:** Scale, latency or availability targets, deadline, team size, systems you couldn't change.
- **Your role:** What you owned, what you contributed to, and what you influenced without owning.

*Likely probes:* Why was this worth doing at that time? What would have happened if nobody did it?

## 2. Architecture

- **Diagram:** One you can draw in two minutes. Components, data flow, and where state lives.
- **Key numbers:** Requests per second, data volume, latency targets, availability target, cost.
- **Data and consistency:** Data model, partitioning, and which guarantees each kind of data needed.

*Likely probes:* Walk me through a request. Where is the bottleneck? What happens when this component fails?

## 3. Decisions and alternatives

| Decision | Options considered | Chosen | Why | What it cost |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

*Likely probes:* Why not the alternative? Who disagreed, and how was it resolved? Would you choose the same today?

## 4. Execution and migration

- **Path from old to new:** Phases, dual writes, backfills, shadow traffic, feature flags, cutover.
- **Rollback plan:** How you would have reverted at each phase.
- **Coordination:** Which teams were involved and how work was sequenced.

*Likely probes:* What was the riskiest step? How did you know it was safe to proceed?

## 5. What went wrong

- **Failures:** Incidents, wrong assumptions, missed estimates.
- **Response:** How it was detected, how it was fixed, and what changed afterward.

*Likely probes:* What was the worst day? What did the postmortem change in the design or the process?

## 6. Results

- **Before and after:** Latency, reliability, cost, developer velocity, or whatever the project targeted.
- **Adoption and follow-on work:** Who uses it now and what it made possible.

*Likely probes:* How did you measure that? What didn't improve?

## 7. Scope and influence

- **Beyond your team:** Decisions you drove that affected other teams or the broader architecture.
- **Alignment:** Who had to agree, where there was resistance, and how you got to a decision.
- **Lasting effects:** People you grew, standards or patterns others adopted, what outlived your involvement.

*Likely probes:* What would not have happened without you specifically?

## 8. Retrospective

- **Hindsight:** What you would do differently.
- **At 10x:** What breaks first and how the design would need to change.
- **Current state:** Known debt and what you'd tell the next owner.

*Likely probes:* If you started over today with current tools, what changes?

---

## Numbers at hand

| Scale | Latency | Availability | Cost | Team size | Timeline |
|---|---|---|---|---|---|
| | | | | | |

## Ready check

- [ ] I can tell it in two minutes and sustain thirty minutes of follow-ups.
- [ ] Every "we" can be broken down into what I personally did.
- [ ] There is at least one decision I would now make differently, and I can say why.
- [ ] I can defend each rejected alternative, not just the chosen one.
- [ ] Numbers are accurate, and confidential details are generalized.
