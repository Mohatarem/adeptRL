from .base.actor_module import ActorModule
from .ac_rollout import ACRolloutActorTrain
from .ac_ppo import ACPPOActorTrain
from adept.actor.ac_eval import ACActorEval, ACActorEvalSample
from .impala import ImpalaHostActor, ImpalaWorkerActor

ACTOR_REG = [
    ACRolloutActorTrain,
    ACActorEval,
    ACActorEvalSample,
    ACPPOActorTrain,
    ImpalaHostActor,
    ImpalaWorkerActor
]
