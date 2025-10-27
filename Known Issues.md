**# Known Issues in `inventory\_system.py`**



**| Issue | Type | Line(s) | Description | Fix Approach |**

**|--------|--------|----------|--------------|----------------|**

**| Missing module docstring | Pylint | 1 | The file lacks a top-level docstring describing its purpose. | Add a brief module-level docstring at the top (e.g., `"""Inventory management system module."""`). |**

**| Unused import | Flake8 / Pylint | 2 | `logging` is imported but not used anywhere in the code. | Remove the unused `import logging` statement. |**

**| Function naming not in snake\_case | Pylint | 8, 14, 22, 25, 31, 36, 41 | Function names like `addItem`, `removeItem`, etc., don’t follow Python naming conventions. | Rename functions using snake\_case (e.g., `add\_item`, `remove\_item`, etc.). |**

**| Dangerous default argument | Pylint | 8 | Default mutable argument `logs=\[]` can lead to shared state across calls. | Use `None` as the default and initialize within the function (`logs = logs or \[]`). |**

**| Missing function docstrings | Pylint | Multiple | Each function lacks a docstring explaining its behavior and arguments. | Add concise docstrings for all functions. |**

**| String formatting not using f-string | Pylint | 12 | Uses old `%` formatting style instead of modern f-string. | Replace with f-string (e.g., `f"{datetime.now()}: Added {qty} of {item}"`). |**

**| Bare `except` block | Bandit / Flake8 / Pylint | 19 | `except:` without specifying exception type hides all errors. | Catch specific exceptions (e.g., `except KeyError:`) or handle properly. |**

**| Try-Except-Pass pattern | Bandit | 19 | `try-except-pass` pattern suppresses all errors, possibly hiding bugs. | Log or handle exceptions meaningfully instead of silently passing. |**

**| Missing blank lines between functions | Flake8 | 8, 14, 22, 25, 31, 36, 41, 48 | Violates PEP8 spacing convention (2 blank lines before top-level function definitions). | Add appropriate blank lines for readability and style compliance. |**

**| Use of `open()` without context manager | Pylint | 26, 32 | Files are opened manually and closed later instead of using `with open(...) as f:`. | Use context managers (`with open(file, "r", encoding="utf-8") as f:`). |**

**| No encoding specified in `open()` | Pylint | 26, 32 | Opening files without specifying encoding may lead to issues across environments. | Add `encoding="utf-8"` when opening files. |**

**| Use of global statement | Pylint | 27 | `global stock\_data` used unnecessarily. | Refactor to avoid modifying global variables directly; consider returning updated data. |**

**| Use of `eval()` | Bandit / Pylint | 59 | `eval()` executes arbitrary code, posing a security risk. | Replace with safer alternatives like `ast.literal\_eval` or avoid dynamic execution entirely. |**

**| Missing blank line after function/class definition | Flake8 | 61 | Missing required blank lines after definitions. | Add blank lines as per PEP8 guidelines. |**



**---**



**### Summary**

**- \*\*Total Issues Found:\*\* 14**  

**- \*\*High-Risk Issues:\*\* Use of `eval`, Bare `except`, Dangerous default argument.**  

**- \*\*Moderate Issues:\*\* Missing docstrings, style and naming inconsistencies, file handling practices.**  

**- \*\*Low-Risk Issues:\*\* Formatting and spacing violations.**



**---**









**| Issue                                                  | Fixed                                                                      |**

**| ------------------------------------------------------ | ---------------------------------------------------------------------------|**

**| Missing module \& function docstrings                   |  Added full docstrings                                                     |**

**| Unused logging import                                  |  Removed                                                                   |**

**| Function names not in snake\_case                       |  Renamed (e.g., 'addItem' → 'add\_item')                                    |**

**| Dangerous default argument ('logs=\[]')                 |  Changed to `logs=None`                                                    |**

**| Missing type checks                                    |  Added 'TypeError' validation                                              |**

**| Bare 'except:'                                         |  Replaced with specific exceptions ('KeyError', 'FileNotFoundError', etc.) |**

**| Use of eval()                                          |  Removed completely                                                        |**





**Which issues were the easiest to fix, and which were the hardest? Why?**



**ans:**

Hardest: Use of eval() as it was posing security issues.

Easiest: Missing docstrings. The additions were straightforward



**Did the static analysis tools report any false positives? If so, describe one example.**	

**ans:**

The "use of global statement" warning from pylint.



**How would you integrate static analysis tools into your actual software development**

**workflow? Consider continuous integration (CI) or local development practices.** 

**ans:**



Integrating static analysis tools into a software development workflow helps ensure consistent code quality and security from the very beginning of development. Developers can run tools like Flake8, Pylint, and Bandit locally—either through their IDEs or as pre-commit hooks—to catch style violations, logical errors, and potential vulnerabilities before committing code. In a larger setup, these same tools can be integrated into a Continuous Integration (CI) pipeline, so that every push or pull request is automatically checked for compliance, with the build failing if serious issues are detected. This approach creates a continuous feedback loop between developers and the CI system, ensuring that only clean, secure, and maintainable code makes it into the main branch.





**What tangible improvements did you observe in the code quality, readability, or potential**

**robustness after applying the fixes?**



After applying the fixes, the code showed clear and measurable improvements in quality, readability, and robustness. The overall structure became cleaner and more professional — functions now follow consistent snake\_case naming, include clear docstrings, and use modern f-string formatting, making the logic much easier to read and maintain













