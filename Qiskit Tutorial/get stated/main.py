import qiskit
import matplotlib.pyplot as plt
from qiskit import IBMQ, QuantumCircuit, transpile
from qiskit.tools import job_monitor
from qiskit.visualization import plot_histogram, plot_gate_map

IBMQ.save_account('<API TOKEN HERE>')
# Loading your IBM Quantum account(s)
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
backend = provider.get_backend('ibmq_lima')

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
qc.draw(output='mpl')

job = backend.run(transpile(qc, backend=backend), shots=1024)

plt.style.use('dark_background')
plot_histogram(job.result().get_counts())