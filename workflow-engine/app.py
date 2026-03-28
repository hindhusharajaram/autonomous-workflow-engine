import gradio as gr
from main import intel

with gr.Blocks(theme=gr.themes.Soft(primary_hue="slate")) as demo:
    gr.Markdown("# Enterprise Meeting Intelligence")
    gr.Markdown("✔ **Action Extraction** | ✔ **Dependency Mapping** | ✔ **Autonomous Follow-up**")

    with gr.Row():
        with gr.Column(scale=4):
            meeting_input = gr.Textbox(label="Meeting Transcript / Executive Notes", lines=3, placeholder="Type decisions here...")
            with gr.Row():
                run_btn = gr.Button("RUN AUTONOMOUS CYCLE", variant="primary")
                clear_btn = gr.Button("RESET & START NEW SESSION")

    gr.Markdown("### 📊 Live Task Lifecycle")
    task_table = gr.Dataframe(headers=["ID", "Decision", "Owner", "Status", "Progress"], interactive=False)

    gr.Markdown("### 📜 System Audit Trail (Explainable AI)")
    log_table = gr.Dataframe(headers=["Time", "Agent", "Action"], interactive=False)

    run_btn.click(intel.process_cycle, inputs=meeting_input, outputs=[task_table, log_table])
    clear_btn.click(intel.reset, outputs=[task_table, log_table])

demo.launch(debug=True, show_error=True)
