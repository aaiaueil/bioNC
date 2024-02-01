import numpy as np
import pytest
from casadi import DM

from bionc import InverseKinematics, NaturalCoordinates
from bionc.bionc_numpy.enums import *
from utils import TestUtils


Q_initialize = NaturalCoordinates(
    np.array(
        [
            [0.92552507, 0.92635303],
            [0.15508409, 0.16741262],
            [-0.34547399, -0.3374064],
            [-1.16229475, -1.16190581],
            [0.0169361, 0.01460067],
            [0.99478173, 0.99296452],
            [-1.08754552, -1.08606826],
            [0.04183331, 0.04094961],
            [0.87313704, 0.87208607],
            [0.11640169, 0.11626677],
            [-0.9846769, -0.98618509],
            [-0.12985393, -0.11798734],
            [0.99453482, 0.99854736],
            [0.10434865, -0.05340154],
            [-0.00344213, -0.00717304],
            [-1.07680923, -1.07537152],
            [-0.04898819, -0.04978109],
            [0.86115999, 0.86123103],
            [-1.07825851, -1.07872174],
            [-0.04875016, -0.05714711],
            [0.44963299, 0.44969122],
            [0.10274889, -0.05091842],
            [-0.97237369, -0.9787783],
            [0.2095998, 0.19849523],
            [0.92327819, 0.94348404],
            [-0.19265789, 0.08574999],
            [0.33232563, 0.32013248],
            [-1.0982818, -1.096765],
            [0.13265481, 0.13168031],
            [0.88511409, 0.8829411],
            [-0.95935303, -0.9598459],
            [0.10551044, 0.11838626],
            [0.48340122, 0.48297849],
            [-0.17083418, 0.10487366],
            [-0.98080731, -0.99355774],
            [-0.09398252, -0.04294801],
            [0.67225558, 0.79179515],
            [-0.61748753, -0.16069423],
            [-0.40838901, -0.58926887],
            [-1.07825851, -1.07872174],
            [-0.04875016, -0.05714711],
            [0.44963299, 0.44969122],
            [-1.33496404, -1.33668599],
            [-0.10761032, -0.11104166],
            [0.11606302, 0.11776413],
            [-0.58654627, -0.21578583],
            [-0.78083032, -0.9761518],
            [0.21509879, -0.02375183],
            [0.78441251, 0.99441088],
            [0.61869921, 0.10423873],
            [0.04368416, 0.01677151],
            [-0.95935303, -0.9598459],
            [0.10551044, 0.11838626],
            [0.48340122, 0.48297849],
            [-0.95452529, -0.95475114],
            [0.12890574, 0.13697615],
            [0.06536438, 0.06536154],
            [0.60415543, 0.09923983],
            [-0.77810908, -0.97704899],
            [0.17187928, 0.18848533],
            [0.79827835, 0.80604966],
            [-0.22489785, -0.16434891],
            [-0.55872411, -0.56857135],
            [-1.33496404, -1.33668599],
            [-0.10761032, -0.11104166],
            [0.11606302, 0.11776413],
            [-1.25961, -1.25726587],
            [-0.13412495, -0.12650836],
            [0.03309571, 0.03188081],
            [-0.54618771, -0.62009157],
            [-0.83526991, -0.77752289],
            [0.06327045, -0.10461638],
            [0.98875687, 0.99253124],
            [0.12935761, 0.08369011],
            [-0.07500973, -0.08875648],
            [-0.95452529, -0.95475114],
            [0.12890574, 0.13697615],
            [0.06536438, 0.06536154],
            [-0.84407189, -0.84421523],
            [0.15209053, 0.14089291],
            [0.02726599, 0.02746627],
            [0.54202173, 0.51158194],
            [-0.82460191, -0.65801452],
            [0.16200042, 0.55254033],
        ]
    )
)

experimental_markers = np.array(
    [
        [
            [-0.99512893, -0.99511677],
            [-1.02508819, -1.0245254],
            [-1.1552875, -1.15531087],
            [-1.16930199, -1.169083],
            [-1.07241082, -1.0696162],
            [-1.08410621, -1.08112752],
            [-0.94997555, -0.95119309],
            [-0.96873051, -0.96978855],
            [-1.35851967, -1.35799468],
            [-1.3114084, -1.3112303],
            [-0.97949064, -0.98210907],
            [-0.92955995, -0.93213236],
            [-1.39764822, -1.39714336],
            [-1.23721457, -1.23893678],
            [-1.28200543, -1.28266609],
            [-1.01061773, -1.01343119],
            [-0.8215977, -0.82410777],
            [-0.86654609, -0.86893791],
        ],
        [
            [-0.08428027, -0.08365151],
            [0.16915414, 0.16987239],
            [-0.04029829, -0.03917728],
            [0.0741705, 0.07526213],
            [-0.10409034, -0.10354505],
            [0.00659003, 0.00701484],
            [0.1593492, 0.15984261],
            [0.05167168, 0.05210308],
            [-0.13896838, -0.13885656],
            [-0.07625225, -0.07610498],
            [0.16105932, 0.16058722],
            [0.09675215, 0.0964836],
            [-0.09523564, -0.09531972],
            [-0.09987623, -0.09949642],
            [-0.16837367, -0.167971],
            [0.13030158, 0.12955573],
            [0.11789952, 0.11763644],
            [0.18628153, 0.18631244],
        ],
        [
            [0.92126387, 0.92181492],
            [0.95468545, 0.95495188],
            [0.98916602, 0.98961705],
            [1.00039744, 1.00072575],
            [0.46156183, 0.46162155],
            [0.43770415, 0.43769968],
            [0.48856014, 0.48850757],
            [0.47824231, 0.47793096],
            [0.12470137, 0.12716728],
            [0.10742468, 0.10935797],
            [0.05826186, 0.05896187],
            [0.07246689, 0.07210413],
            [0.12971023, 0.13277037],
            [0.03050142, 0.03068059],
            [0.03568999, 0.03723054],
            [0.0399006, 0.04101478],
            [0.03398312, 0.03370571],
            [0.02054886, 0.02053879],
        ],
    ]
)


def test_user_provided():
    bionc = TestUtils.bionc_folder()
    module = TestUtils.load_module(bionc + "/examples/model_creation/marker_model.py")

    c3d_filename = module.generate_c3d_file()

    ik = InverseKinematics(
        model=module.model_creation_markers(c3d_filename, False),
        experimental_markers=experimental_markers,
        solve_frame_per_frame=True,
    )
    ik.solve(Q_init=Q_initialize, initial_guess_mode=InitialGuessModeType.USER_PROVIDED, method="ipopt")

    TestUtils.assert_equal(
        ik.Qopt,
        np.array(
            [
                [9.26353029e-01, 9.26536852e-01],
                [1.67412619e-01, 1.65664974e-01],
                [-3.37406404e-01, -3.37764086e-01],
                [-1.16190581e00, -1.16178929e00],
                [1.46006734e-02, 1.55841393e-02],
                [9.92964519e-01, 9.93382340e-01],
                [-1.08606826e00, -1.08596905e00],
                [4.09496107e-02, 4.19466231e-02],
                [8.72086066e-01, 8.72495979e-01],
                [1.16266766e-01, 1.13721116e-01],
                [-9.86185087e-01, -9.86272790e-01],
                [-1.17987345e-01, -1.19722557e-01],
                [9.98547356e-01, 9.98839832e-01],
                [-5.34015438e-02, -4.81557825e-02],
                [-7.17304072e-03, -9.97474680e-05],
                [-1.07537152e00, -1.07550652e00],
                [-4.97810912e-02, -4.87921477e-02],
                [8.61231030e-01, 8.61481300e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-5.09184242e-02, -4.71733002e-02],
                [-9.78778299e-01, -9.78873433e-01],
                [1.98495227e-01, 1.98950952e-01],
                [9.43484042e-01, 9.44461913e-01],
                [8.57499899e-02, 8.78584799e-02],
                [3.20132476e-01, 3.16658463e-01],
                [-1.09676500e00, -1.09643159e00],
                [1.31680313e-01, 1.32685394e-01],
                [8.82941102e-01, 8.83510657e-01],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [1.04873655e-01, 1.06302662e-01],
                [-9.93557741e-01, -9.93471016e-01],
                [-4.29480136e-02, -4.14135854e-02],
                [7.91795150e-01, 7.87578735e-01],
                [-1.60694225e-01, -1.58958119e-01],
                [-5.89268875e-01, -5.95358759e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-2.15785826e-01, -2.13758685e-01],
                [-9.76151796e-01, -9.76638386e-01],
                [-2.37518290e-02, -2.20156227e-02],
                [9.94410882e-01, 9.94296039e-01],
                [1.04238734e-01, 1.05843316e-01],
                [1.67715058e-02, 1.31369791e-02],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [9.92398305e-02, 1.01441500e-01],
                [-9.77048993e-01, -9.76528226e-01],
                [1.88485334e-01, 1.90005913e-01],
                [8.06049659e-01, 7.96144159e-01],
                [-1.64348908e-01, -1.61105442e-01],
                [-5.68571353e-01, -5.83266247e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-1.25726587e00, -1.25841099e00],
                [-1.26508363e-01, -1.26093674e-01],
                [3.18808141e-02, 3.26896682e-02],
                [-6.20091574e-01, -6.19938176e-01],
                [-7.77522895e-01, -7.78854496e-01],
                [-1.04616384e-01, -9.51962779e-02],
                [9.92531235e-01, 9.92119120e-01],
                [8.36901089e-02, 8.51818486e-02],
                [-8.87564807e-02, -9.18896262e-02],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [-8.44215227e-01, -8.46854365e-01],
                [1.40892907e-01, 1.40669556e-01],
                [2.74662747e-02, 2.71959788e-02],
                [5.11581940e-01, 5.14337664e-01],
                [-6.58014518e-01, -6.56126270e-01],
                [5.52540327e-01, 5.52227385e-01],
            ]
        ),
    )


def test_user_provided_first_frame_only():
    bionc = TestUtils.bionc_folder()
    module = TestUtils.load_module(bionc + "/examples/model_creation/marker_model.py")

    c3d_filename = module.generate_c3d_file()

    ik = InverseKinematics(
        model=module.model_creation_markers(c3d_filename, False),
        experimental_markers=experimental_markers,
        solve_frame_per_frame=True,
    )
    ik.solve(
        Q_init=Q_initialize, initial_guess_mode=InitialGuessModeType.USER_PROVIDED_FIRST_FRAME_ONLY, method="ipopt"
    )

    TestUtils.assert_equal(
        ik.Qopt,
        np.array(
            [
                [9.26353029e-01, 9.26536852e-01],
                [1.67412619e-01, 1.65664974e-01],
                [-3.37406404e-01, -3.37764086e-01],
                [-1.16190581e00, -1.16178929e00],
                [1.46006734e-02, 1.55841393e-02],
                [9.92964519e-01, 9.93382340e-01],
                [-1.08606826e00, -1.08596905e00],
                [4.09496107e-02, 4.19466231e-02],
                [8.72086066e-01, 8.72495979e-01],
                [1.16266766e-01, 1.13721116e-01],
                [-9.86185087e-01, -9.86272790e-01],
                [-1.17987345e-01, -1.19722557e-01],
                [9.98547356e-01, 9.98839832e-01],
                [-5.34015438e-02, -4.81557825e-02],
                [-7.17304072e-03, -9.97474680e-05],
                [-1.07537152e00, -1.07550652e00],
                [-4.97810912e-02, -4.87921477e-02],
                [8.61231030e-01, 8.61481300e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-5.09184242e-02, -4.71733002e-02],
                [-9.78778299e-01, -9.78873433e-01],
                [1.98495227e-01, 1.98950952e-01],
                [9.43484042e-01, 9.44461913e-01],
                [8.57499899e-02, 8.78584799e-02],
                [3.20132476e-01, 3.16658463e-01],
                [-1.09676500e00, -1.09643159e00],
                [1.31680313e-01, 1.32685394e-01],
                [8.82941102e-01, 8.83510657e-01],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [1.04873655e-01, 1.06302662e-01],
                [-9.93557741e-01, -9.93471016e-01],
                [-4.29480136e-02, -4.14135854e-02],
                [7.91795150e-01, 7.87578735e-01],
                [-1.60694225e-01, -1.58958119e-01],
                [-5.89268875e-01, -5.95358759e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-2.15785826e-01, -2.13758685e-01],
                [-9.76151796e-01, -9.76638386e-01],
                [-2.37518290e-02, -2.20156227e-02],
                [9.94410882e-01, 9.94296039e-01],
                [1.04238734e-01, 1.05843316e-01],
                [1.67715058e-02, 1.31369791e-02],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [9.92398305e-02, 1.01441500e-01],
                [-9.77048993e-01, -9.76528226e-01],
                [1.88485334e-01, 1.90005913e-01],
                [8.06049659e-01, 7.96144159e-01],
                [-1.64348908e-01, -1.61105442e-01],
                [-5.68571353e-01, -5.83266247e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-1.25726587e00, -1.25841099e00],
                [-1.26508363e-01, -1.26093674e-01],
                [3.18808141e-02, 3.26896682e-02],
                [-6.20091574e-01, -6.19938176e-01],
                [-7.77522895e-01, -7.78854496e-01],
                [-1.04616384e-01, -9.51962779e-02],
                [9.92531235e-01, 9.92119120e-01],
                [8.36901089e-02, 8.51818486e-02],
                [-8.87564807e-02, -9.18896262e-02],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [-8.44215227e-01, -8.46854365e-01],
                [1.40892907e-01, 1.40669556e-01],
                [2.74662747e-02, 2.71959788e-02],
                [5.11581940e-01, 5.14337664e-01],
                [-6.58014518e-01, -6.56126270e-01],
                [5.52540327e-01, 5.52227385e-01],
            ]
        ),
    )


def test_from_current_markers():
    bionc = TestUtils.bionc_folder()
    module = TestUtils.load_module(bionc + "/examples/model_creation/marker_model.py")

    c3d_filename = module.generate_c3d_file()

    ik = InverseKinematics(
        model=module.model_creation_markers(c3d_filename, False),
        experimental_markers=experimental_markers,
        solve_frame_per_frame=True,
    )
    ik.solve(initial_guess_mode=InitialGuessModeType.FROM_CURRENT_MARKERS, method="ipopt")

    TestUtils.assert_equal(
        ik.Qopt,
        np.array(
            [
                [9.26353029e-01, 9.26536852e-01],
                [1.67412619e-01, 1.65664974e-01],
                [-3.37406404e-01, -3.37764086e-01],
                [-1.16190581e00, -1.16178929e00],
                [1.46006734e-02, 1.55841393e-02],
                [9.92964519e-01, 9.93382340e-01],
                [-1.08606826e00, -1.08596905e00],
                [4.09496107e-02, 4.19466231e-02],
                [8.72086066e-01, 8.72495979e-01],
                [1.16266766e-01, 1.13721116e-01],
                [-9.86185087e-01, -9.86272790e-01],
                [-1.17987345e-01, -1.19722557e-01],
                [9.98547356e-01, 9.98839832e-01],
                [-5.34015438e-02, -4.81557825e-02],
                [-7.17304072e-03, -9.97474680e-05],
                [-1.07537152e00, -1.07550652e00],
                [-4.97810912e-02, -4.87921477e-02],
                [8.61231030e-01, 8.61481300e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-5.09184242e-02, -4.71733002e-02],
                [-9.78778299e-01, -9.78873433e-01],
                [1.98495227e-01, 1.98950952e-01],
                [9.43484042e-01, 9.44461913e-01],
                [8.57499899e-02, 8.78584799e-02],
                [3.20132476e-01, 3.16658463e-01],
                [-1.09676500e00, -1.09643159e00],
                [1.31680313e-01, 1.32685394e-01],
                [8.82941102e-01, 8.83510657e-01],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [1.04873655e-01, 1.06302662e-01],
                [-9.93557741e-01, -9.93471016e-01],
                [-4.29480136e-02, -4.14135854e-02],
                [7.91795150e-01, 7.87578735e-01],
                [-1.60694225e-01, -1.58958119e-01],
                [-5.89268875e-01, -5.95358759e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-2.15785826e-01, -2.13758685e-01],
                [-9.76151796e-01, -9.76638386e-01],
                [-2.37518290e-02, -2.20156227e-02],
                [9.94410882e-01, 9.94296039e-01],
                [1.04238734e-01, 1.05843316e-01],
                [1.67715058e-02, 1.31369791e-02],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [9.92398305e-02, 1.01441500e-01],
                [-9.77048993e-01, -9.76528226e-01],
                [1.88485334e-01, 1.90005913e-01],
                [8.06049659e-01, 7.96144159e-01],
                [-1.64348908e-01, -1.61105442e-01],
                [-5.68571353e-01, -5.83266247e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-1.25726587e00, -1.25841099e00],
                [-1.26508363e-01, -1.26093674e-01],
                [3.18808141e-02, 3.26896682e-02],
                [-6.20091574e-01, -6.19938176e-01],
                [-7.77522895e-01, -7.78854496e-01],
                [-1.04616384e-01, -9.51962779e-02],
                [9.92531235e-01, 9.92119120e-01],
                [8.36901089e-02, 8.51818486e-02],
                [-8.87564807e-02, -9.18896262e-02],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [-8.44215227e-01, -8.46854365e-01],
                [1.40892907e-01, 1.40669556e-01],
                [2.74662747e-02, 2.71959788e-02],
                [5.11581940e-01, 5.14337664e-01],
                [-6.58014518e-01, -6.56126270e-01],
                [5.52540327e-01, 5.52227385e-01],
            ]
        ),
    )


def test_from_first_frame_markers():
    bionc = TestUtils.bionc_folder()
    module = TestUtils.load_module(bionc + "/examples/model_creation/marker_model.py")

    c3d_filename = module.generate_c3d_file()

    ik = InverseKinematics(
        model=module.model_creation_markers(c3d_filename, False),
        experimental_markers=experimental_markers,
        solve_frame_per_frame=True,
    )
    ik.solve(initial_guess_mode=InitialGuessModeType.FROM_FIRST_FRAME_MARKERS, method="ipopt")

    TestUtils.assert_equal(
        ik.Qopt,
        np.array(
            [
                [9.26353029e-01, 9.26536852e-01],
                [1.67412619e-01, 1.65664974e-01],
                [-3.37406404e-01, -3.37764086e-01],
                [-1.16190581e00, -1.16178929e00],
                [1.46006734e-02, 1.55841393e-02],
                [9.92964519e-01, 9.93382340e-01],
                [-1.08606826e00, -1.08596905e00],
                [4.09496107e-02, 4.19466231e-02],
                [8.72086066e-01, 8.72495979e-01],
                [1.16266766e-01, 1.13721116e-01],
                [-9.86185087e-01, -9.86272790e-01],
                [-1.17987345e-01, -1.19722557e-01],
                [9.98547356e-01, 9.98839832e-01],
                [-5.34015438e-02, -4.81557825e-02],
                [-7.17304072e-03, -9.97474680e-05],
                [-1.07537152e00, -1.07550652e00],
                [-4.97810912e-02, -4.87921477e-02],
                [8.61231030e-01, 8.61481300e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-5.09184242e-02, -4.71733002e-02],
                [-9.78778299e-01, -9.78873433e-01],
                [1.98495227e-01, 1.98950952e-01],
                [9.43484042e-01, 9.44461913e-01],
                [8.57499899e-02, 8.78584799e-02],
                [3.20132476e-01, 3.16658463e-01],
                [-1.09676500e00, -1.09643159e00],
                [1.31680313e-01, 1.32685394e-01],
                [8.82941102e-01, 8.83510657e-01],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [1.04873655e-01, 1.06302662e-01],
                [-9.93557741e-01, -9.93471016e-01],
                [-4.29480136e-02, -4.14135854e-02],
                [7.91795150e-01, 7.87578735e-01],
                [-1.60694225e-01, -1.58958119e-01],
                [-5.89268875e-01, -5.95358759e-01],
                [-1.07872174e00, -1.07591946e00],
                [-5.71471145e-02, -5.65048592e-02],
                [4.49691223e-01, 4.49934416e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-2.15785826e-01, -2.13758685e-01],
                [-9.76151796e-01, -9.76638386e-01],
                [-2.37518290e-02, -2.20156227e-02],
                [9.94410882e-01, 9.94296039e-01],
                [1.04238734e-01, 1.05843316e-01],
                [1.67715058e-02, 1.31369791e-02],
                [-9.59845899e-01, -9.60893187e-01],
                [1.18386264e-01, 1.18840459e-01],
                [4.82978489e-01, 4.83096717e-01],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [9.92398305e-02, 1.01441500e-01],
                [-9.77048993e-01, -9.76528226e-01],
                [1.88485334e-01, 1.90005913e-01],
                [8.06049659e-01, 7.96144159e-01],
                [-1.64348908e-01, -1.61105442e-01],
                [-5.68571353e-01, -5.83266247e-01],
                [-1.33668599e00, -1.33631862e00],
                [-1.11041658e-01, -1.11010380e-01],
                [1.17764132e-01, 1.20014434e-01],
                [-1.25726587e00, -1.25841099e00],
                [-1.26508363e-01, -1.26093674e-01],
                [3.18808141e-02, 3.26896682e-02],
                [-6.20091574e-01, -6.19938176e-01],
                [-7.77522895e-01, -7.78854496e-01],
                [-1.04616384e-01, -9.51962779e-02],
                [9.92531235e-01, 9.92119120e-01],
                [8.36901089e-02, 8.51818486e-02],
                [-8.87564807e-02, -9.18896262e-02],
                [-9.54751145e-01, -9.57269489e-01],
                [1.36976149e-01, 1.36638953e-01],
                [6.53615371e-02, 6.54299349e-02],
                [-8.44215227e-01, -8.46854365e-01],
                [1.40892907e-01, 1.40669556e-01],
                [2.74662747e-02, 2.71959788e-02],
                [5.11581940e-01, 5.14337664e-01],
                [-6.58014518e-01, -6.56126270e-01],
                [5.52540327e-01, 5.52227385e-01],
            ]
        ),
    )
