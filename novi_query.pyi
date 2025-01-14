from typing import Any

class TagGraph:
    def collect_tags(self) -> list[str]: ...

class Query:
    def is_match(self, graph: TagGraph) -> bool: ...
    def to_sql(self, args: list[Any]) -> str: ...
    def meta_queries(self) -> list[tuple[bool, str, str]]: ...

def parse_tag_graph(graph: str, validate: bool = True) -> TagGraph: ...
def parse_query(query: str, validate: bool = True) -> Query: ...
def set_meta_query_matcher(patterns: list[str]) -> None: ...