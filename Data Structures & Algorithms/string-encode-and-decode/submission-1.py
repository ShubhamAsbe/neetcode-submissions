class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract string
            result.append(s[j:j + length])

            # Move to next encoded string
            i = j + length

        return result