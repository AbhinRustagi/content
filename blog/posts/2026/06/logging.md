---
title: More logs ≠ Better logs
slug: logging
canonical_url: https://www.abhin.dev/blog/logging
date: 2026-06-19
published: true
tags:
  - Backend Development
  - Observability
  - Logging
description: What to log? When to log? Where to log? An informal handbook to write logs
reading_time: 5
---

I reckon a lot of people have been there - what to log? when to log? where to log? (and sometimes) how to log it? In my opinion, a good stream of logs should be able to tell a simple story - a story you want to make sense, and a story where you don't want to be reading between the lines. Logging provides observability at the ground level and gives visibility into the chaos of runtime. 

Imagine this - something in production breaks, and you have no idea what. All the systems are online and responding, but you're not sure what it is. One of the first places you look is your log aggregation tool. The logs report that there was an API request and something broke without a proper stack trace or error message.

I've been there. I started off writing logs like this:

```python
def do_something():
  try:
    Logger.info("Starting to do something")
    a = sub_do_something_pt_1()
    Logger.info(f"sub_do_something_pt_1 succeeded with {a}")
    b = sub_do_something_pt_2()
    Logger.info(f"sub_do_something_pt_1 succeeded with {b}")
    return a + b
  except Exception as e:
    Logger.error(f"do_something had an error = {str(e)}")
```

That's as ugly as it comes. The problem was that the logs answered the wrong questions. All technically correct. All completely useless. Over time, I realized that good logs aren't about recording execution. They're about recording decisions.

That shift changed the way I write logs more than any logging library or observability tool ever did.

Biggest challenge figuring out the logging methods was standardising a format to write them. That's when I found [logfmt](https://www.cloudbees.com/blog/logfmt-a-log-format-thats-easy-to-read-and-write) - as simple as it comes, as easy to read. 

Another thing I strived to solve for was reproducability. An application error that broke because of an issue in your business logic implementation should be figurable through your logs. You need your input stream so you can reproduce how data flowed, transformed, and where it broke something. (A helpful tool there is also your debugger!)

I fell in love with logfmt logs. Look how beautiful:

```
INFO request_id=123 msg="Received checkout request" order_id=1892A user_id=7G35JA
INFO request_id=123 msg="Payment Authorized" amt=1499
WARN request_id=456 msg="Inventory Service Timeout" retry=2
```

## The rules I try to follow now

I don't claim these are universal, but they've worked well for me.

### Log decisions, not execution

This: `Calling payment service` tells me almost nothing.

This: `INFO request_id=123 msg="Payment Authorized" provider=stripe amt=1499` tells me that a business event happened. The code already tells me which function was called. The logs should tell me what the system decided.

### Log boundaries

Those are usually worth logging. The fifth helper function inside your validation pipeline probably isn't.

### Give errors context

This: `ERROR database timeout` becomes: `ERROR request_id=123 msg="Failed to reserve inventory" warehouse_id=12 retry=3 timeout_ms=5000` The exception tells me where it failed. The surrounding fields tell me why.

### Make logs reproducible

One of the questions I increasingly ask myself is: Could I reproduce this issue from the logs alone?

If the answer is no, I probably haven't logged enough context. Input identifiers, request IDs, retries, state transitions, and external responses often matter far more than the stack trace itself.

## Final Thoughts

If I'm staring at CloudWatch at 2 AM trying to understand an outage, I want my past self to have left me a story instead of a transcript.

## Related stuff I found interesting

- [On Observability and Logging](https://medium.com/unomaly/on-observability-and-logging-10848b2e1d5d?ref=)
- [Logging Wisdom: How to Log](https://medium.com/unomaly/logging-wisdom-how-to-log-5a19145e35ec?ref=)
- [Mastering Logging in Software Development: Best Practices, Strategies, and Real-World Azure Integration](https://medium.com/@dhiaedd.sn/mastering-logging-in-software-development-best-practices-strategies-and-real-world-azure-9adb2e2a9eaa)
- [Getting Logging Right: Observability Foundation](https://hackernoon.com/getting-logging-right-observability-foundation)
- [The Question Your Observability Vendor Won't Answer](https://usetero.com/blog/the-question-your-observability-vendor-wont-answer/)
