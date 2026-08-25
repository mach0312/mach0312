# Hi, I'm Jaerak Son 👋

Robotics engineer working on **motion planning and control for mobile robots**.

I like working across the whole vertical slice rather than a single layer of it — deriving the
kinematics, writing the controller, wiring it into ROS 2, putting it in simulation, and then
building the experiment that shows whether it actually holds up. Most of what I publish here is
one piece of that loop.

- 🤖 Motion planning & control at **PIT-IN (피트인)**
- 📄 **ICROS 2026** — precision docking control for an omnidirectional AMR
- 🎓 Sampling-based planning lecture series — PRM, RRT, RRT\*, Informed RRT\*
- 📫 Reach me at **jr@pitin-ev.com**

<p>
  <img alt="ROS 2" src="https://img.shields.io/badge/ROS%202-Jazzy%20%7C%20Humble-22314E?style=flat-square&logo=ros&logoColor=white">
  <img alt="C++17" src="https://img.shields.io/badge/C%2B%2B-17-00599C?style=flat-square&logo=cplusplus&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="ros2_control" src="https://img.shields.io/badge/ros2__control-1f6feb?style=flat-square">
  <img alt="Nav2" src="https://img.shields.io/badge/Nav2-3fb950?style=flat-square">
  <img alt="Gazebo" src="https://img.shields.io/badge/Gazebo-FB8C00?style=flat-square&logo=gazebo&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
</p>

## What I work on

- **Mobile robot kinematics and control** — omnidirectional and steerable-wheel platforms
- **Motion planning** — sampling-based planners and sampling-based MPC
- **Controller design for precision tasks** — sensor-feedback control where the tolerance is
  millimetres rather than centimetres
- **Simulation-to-hardware workflows** — the same controller running in Gazebo and on the robot
- **Reproducible evaluation** — benchmarks and analysis that someone else can re-run

## Publication

**Kinematic-based Precision Docking Controller for a Double-Steering-Drive Omni AMR**
Jaerak Son · *ICROS Annual Conference 2026*
Code and experiments: [`omni-docking-bench`](https://github.com/mach0312/omni-docking-bench)

## Selected repositories

| Repository | What it is | Stack |
|---|---|---|
| [omni-docking-bench](https://github.com/mach0312/omni-docking-bench) | Reproducibility package for the ICROS 2026 docking paper — experiment runner, analysis and plots | Python · ROS 2 |
| [double_steering_drive_controller](https://github.com/mach0312/double_steering_drive_controller) | `ros2_control` controller plugin for a double-steering-drive platform | C++ |
| [dsd_control_demo](https://github.com/mach0312/dsd_control_demo) | Hardware interface and bringup for the same platform | C++ · ros2_control |
| [dsd_bot_description](https://github.com/mach0312/dsd_bot_description) | Robot description (URDF / xacro) | xacro |
| [pgv_tracing_mode](https://github.com/mach0312/pgv_tracing_mode) | Line tracing and pose alignment from a guidance sensor | Python · ROS 2 |
| [payload_mass_estimator](https://github.com/mach0312/payload_mass_estimator) | Online payload mass estimation for mobile robots | C++ · ROS 2 |
| [Sampling-Based-Planning_Tutorial](https://github.com/mach0312/Sampling-Based-Planning_Tutorial) | Lecture implementations of classic sampling-based planners | Python |

## Teaching

Sampling-based planning lecture material written for **RCI Lab, Kyung Hee University** —
PRM, RRT, RRT\*, Informed RRT\* and Connect-RRT, implemented from scratch in Python.

[![Lecture playlist](https://img.shields.io/badge/Lecture%20playlist-YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://youtube.com/playlist?list=PL5zS4AjTJMs8wwZQyWds0j8TPxq3N_OpD)

## Reading list

Repositories I keep forked as references. These are **upstream work by
[RCILab](https://github.com/RCILab) and [behnamasadi](https://github.com/behnamasadi), not my own
code** — they are here because I read and run them:

`RCI_quadruped_robot_navigation` · `RCI_cscmppi` · `RCI_hybrid_astar_guided_mppi` ·
`RCI_radiation` · `robotic_notes` · `bench-mr`

## Contact

[![Email](https://img.shields.io/badge/jr@pitin--ev.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:jr@pitin-ev.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/YOUR-LINKEDIN-HANDLE)

<details>
<summary>Why there are no GitHub stats cards here</summary>

<br>

The `github-readme-stats.vercel.app` cards that used to be on this profile were both broken — the
shared public instance returns `503 DEPLOYMENT_PAUSED`, and `github-profile-trophy` returns `402`.
A card that 503s renders as a broken-image icon, so they were removed rather than replaced.

To bring them back reliably, deploy your own instance: fork
[`anuraghazra/github-readme-stats`](https://github.com/anuraghazra/github-readme-stats), create a
personal access token with no scopes, import the fork into [Vercel](https://vercel.com/new) with
the token set as `PAT_1`, and point the image at your own deployment:

```markdown
![stats](https://YOUR-APP.vercel.app/api?username=mach0312&show_icons=true&theme=github_dark&hide_border=true)
```

</details>
