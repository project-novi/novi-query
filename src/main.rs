use novi_query::parser::parse_tag_graph;

fn main() {
    if let Err(err) = parse_tag_graph("asd[", false) {
        eprintln!("{}", err);
    }
}
