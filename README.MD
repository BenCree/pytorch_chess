# (silly) Chess Engine in PyTorch
## Plan

1. get training data from public database in parsable format
2. parse data
3. train model
3i. optimise model
4. use model to score search tree
5. search tree with some known method something something monte carlo
6. ???
7. win chess

maybe score each state with an engine and train model to predict score, then pick best scoring move.
learning result from gamestates isn't a good idea e.g. blunder early on but still won, 
has no measure of how good an individual state is, just that it eventually ended up winning, 
but will set up infrastructure for more complicated things.
