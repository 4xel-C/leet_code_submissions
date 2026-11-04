"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """Strategy: Split the string and use a stack to track the menu arborescence."""
        stack_menu = []

        path_list = path.split("/")

        for subpath in path_list:
            # Don't move from the current directory
            if subpath == "." or subpath == "":
                continue

            # Get down one level
            elif subpath == "..":
                if len(stack_menu) > 0:
                    stack_menu.pop()

            # else, append the new path
            else:
                stack_menu.append(subpath)

        # prepend with the root directory
        return "/" + "/".join(stack_menu)


if __name__ == "__main__":
    solver = Solution()
    path = "/../"

    print(solver.simplifyPath(path))
