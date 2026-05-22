import streamlit.components.v1 as components


def scroll_to_latest_message() -> None:
    """Scroll conversation box and main view to the latest message."""
    components.html(
        """
        <script>
        (function () {
            const doc = window.parent.document;

            function scrollAll() {
                const anchor = doc.querySelector(".conv-scroll-anchor");

                doc.querySelectorAll(
                    '[data-testid="stVerticalBlockBorderWrapper"]'
                ).forEach(function (wrapper) {
                    wrapper.scrollTop = wrapper.scrollHeight;
                    wrapper.querySelectorAll("div").forEach(function (el) {
                        if (el.scrollHeight > el.clientHeight + 2) {
                            el.scrollTop = el.scrollHeight;
                        }
                    });
                });

                const main =
                    doc.querySelector('[data-testid="stAppViewContainer"]') ||
                    doc.querySelector("section.main") ||
                    doc.documentElement;

                if (main && main.scrollHeight > main.clientHeight) {
                    main.scrollTop = main.scrollHeight;
                }

                if (anchor) {
                    anchor.scrollIntoView({ block: "end", behavior: "auto" });
                }

                try {
                    window.parent.scrollTo({
                        top: doc.body.scrollHeight,
                        behavior: "auto",
                    });
                } catch (e) {}
            }

            scrollAll();
            requestAnimationFrame(scrollAll);
            setTimeout(scrollAll, 80);
            setTimeout(scrollAll, 200);
            setTimeout(scrollAll, 500);
            setTimeout(scrollAll, 900);
        })();
        </script>
        """,
        height=0,
        width=0,
    )
