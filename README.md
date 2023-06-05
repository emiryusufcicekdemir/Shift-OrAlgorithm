# Shift-OrAlgorithm
The Shift-Or algorithm is a string matching algorithm used to compare two texts and determine whether one exists as a subtext of the other.

The basic logic of the algorithm is to perform the matching using a preprocessed mask table and shift operations. The mask table is a bit mask sequence that determines which of the characters in the text to be searched match the characters in the searched text. The shift operation is the operation of shifting the searched text to the right.

The Shift-Or algorithm creates the mask table in the first step and shifts the searched text to the right in the second step. During each scrolling operation, it is checked whether the characters specified in the mask table match the characters in the searched text. If a match is found, the subtext in the searched text has been found.

The Shift-Or algorithm is somewhat memory-intensive due to its size and preprocessed mask table. However, it is fast compared to some other string matching algorithms and is especially effective for small text. In addition, its extended versions can be used for other problems such as dynamic programming and parallel computing.

-Algorithm Analysis-

The runtime of the Shift-Or algorithm occurs in O(nm/w) time to search for a pattern length m in a text of text length n, where w specifies the word size. This time is added in some amount during the creation of the precomputed mask table.

In the best case, if the pattern never occurs in the text, the runtime of the algorithm will be O(n/w). In this case, the entire text is processed only once and the searched pattern cannot be found.

In the worst case, when there is no exact match between each pattern character and text characters, the algorithm's runtime will be O(nm/w). In this case, m steps are taken for each character of the mask table and search is performed in n - m + 1 steps.

The average case is when the pattern is randomly placed in the text. The Shift-Or algorithm, like other string matching algorithms, does not focus on a particular region of the searched text, so the average case will be O(nm/w).
