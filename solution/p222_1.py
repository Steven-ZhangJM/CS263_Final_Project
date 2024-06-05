*

```python
import math

def calculate_shortest_pipe_length(balls):
    max_radius = max(ball['radius'] for ball in balls)
    min_radius = min(ball['radius'] for ball in balls)

    return int((max_radius + min_radius) * 2.0 + 1e-6)

balls = [{'radius': 30e-3}, {'radius': 31e-3}, {'radius': 32e-3}, ..., {'radius': 50e-3}] * 21

print(calculate_shortest_pipe_length(balls))
```

**